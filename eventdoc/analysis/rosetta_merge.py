import abc

from eventdoc.analysis.result import Event
from rosetta.game.projectzomboid.event import ZomboidEvent
from rosetta.lua.callback import LuaCallback
from rosetta.lua.parameter import LuaParameter


lua_type_name_map: dict[str, str] = {
    "Float": "number",
    "Double": "number",
    "Byte": "integer",
    "Short": "integer",
    "Integer": "integer",
    "Long": "integer",
    "KahluaTableImpl": "table",
    "KahluaTable": "table",
    "KahluaArray": "table",
    "LuaClosure": "function",
    "String": "string",
    "Character": "string",
    "Object": "any",
    "Void": "nil",
    "Boolean": "boolean",
}


def java_type_to_lua_type(type: str) -> str:
    type = type[type.rfind('/') + 1:].replace("$", ".")
    type = lua_type_name_map.get(type, type)
    return type


class RosettaMismatchError:
    def __init__(self, analysed: Event, rosetta: ZomboidEvent, kind: str) -> None:
        self.rosetta: ZomboidEvent = rosetta
        self.analysed: Event = analysed
        self.kind: str = kind


class RosettaParameterTypeError(RosettaMismatchError):
    def __init__(self, analysed: Event, rosetta: ZomboidEvent, index: int, real_type: str, doc_type: str) -> None:
        super().__init__(analysed, rosetta, "parameter_type_mismatch")
        self.index: int = index
        self.real_type: str = real_type
        self.doc_type: str = doc_type


class ErrorHandler(abc.ABC):
    @abc.abstractmethod
    def add_error(self, error: RosettaMismatchError) -> None:
        ...


class PrintErrorHandler(ErrorHandler):
    def add_error(self, error: RosettaMismatchError) -> None:
        match error.kind:
            case "too_many_parameters":
                print(f"Rosetta argument count mismatch: "
                      f"{error.analysed.name} has {len(error.analysed.arguments[0])} arguments, "
                      f"but {len(error.rosetta.callback.parameters)} are documented.")
            case "not_enough_parameters":
                print(f"Rosetta argument count mismatch: "
                      f"{error.analysed.name} has {len(error.analysed.arguments[0])} arguments, "
                      f"but only {len(error.rosetta.callback.parameters)} are documented.")
            case "parameter_type_mismatch":
                assert isinstance(error, RosettaParameterTypeError)
                print(f"Rosetta parameter type mismatch: {error.analysed.name}#{error.index}: "
                      f"got {error.doc_type}, expected {error.real_type}")


def flatten_parameter_types(arguments: list[list[str]]) -> list[str]:
    if len(arguments) <= 0:
        return []

    max_arguments: int = 0
    for argument_list in arguments:
        if len(argument_list) > max_arguments:
            max_arguments = len(argument_list)

    if max_arguments <= 0:
        return []

    parameter_types: list[str] = []
    for i in range(max_arguments):
        argument_types = set()
        for argument_list in arguments:
            if i > len(argument_list) - 1:
                argument_types.add("nil")
            else:
                argument_types.add(
                    java_type_to_lua_type(argument_list[i])
                )

        if "integer" in argument_types and "number" in argument_types:
            argument_types.remove("integer")
        # TODO: use rosetta data to flatten to superclasses
        #  e.g. IsoGameCharacter | IsoPlayer should be flattened to IsoGameCharacter
        #  IsoZombie | IsoPlayer might be flattened to IsoGameCharacter too?

        parameter_types.append(str.join(" | ", argument_types))

    return parameter_types


def is_compatible_type(analysed_type: str, doc_type: str) -> bool:
    doc_is_list: bool = " | " in doc_type
    analysed_is_list: bool = " | " in analysed_type

    if doc_is_list and analysed_is_list:
        # if both are lists, check every analysed type against every doc type
        # as long as every type has at least one match, the types are compatible
        doc_types = doc_type.split(" | ")
        unmatched_doc_types: set[str] = set(doc_types)
        # nullability is hard to analyse, so we trust the doc
        if "nil" in unmatched_doc_types:
            unmatched_doc_types.remove("nil")

        analysed_types = analysed_type.split(" | ")
        unmatched_analysed_types: set[str] = set(analysed_types)

        for analysed in analysed_types:
            for doc in doc_types:
                if is_compatible_type(analysed, doc):
                    unmatched_analysed_types.remove(analysed)
                    unmatched_doc_types.remove(doc)

        if len(unmatched_doc_types) > 0 or len(unmatched_analysed_types) > 0:
            return False
        return True
    elif doc_is_list:
        # multiple types, only return true if all are compatible
        for type in doc_type.split(" | "):
            if type == "nil":
                continue  # nullability is hard to analyse, trust the doc
            if not is_compatible_type(analysed_type, type):
                return False
        return True
    elif analysed_is_list:
        for type in analysed_type.split(" | "):
            if not is_compatible_type(type, doc_type):
                return False
        return True

    if analysed_type == "any":
        # any is only analysed in cases where we can't determine the type
        # reporting these as incompatible would result in far too many false positives
        return True

    # remove all generic arguments, we don't have a way to analyse them, trust the doc
    if doc_type.endswith(">"):
        doc_type = doc_type[:doc_type.find("<")]

    if analysed_type == doc_type:
        return True

    match analysed_type:
        case "integer":
            # also allow integer literals
            try:
                int(doc_type)
                return True
            except ValueError:
                return False
        case "number":
            # also allow float literals
            try:
                float(doc_type)
                return True
            except ValueError:
                return False
        case "string":
            # also allow string literals
            return doc_type.startswith('\"') and doc_type.endswith('\"')
        case "boolean":
            # also allow boolean literals
            return doc_type == "false" or doc_type == "true"

    return False


def convert_event(event: Event, documentation: ZomboidEvent | None = None,
                  error_handler: ErrorHandler | None = None) -> ZomboidEvent:
    converted_event = ZomboidEvent(event.name)

    callback = LuaCallback(f"umbrella.Callback_{event.name}")
    parameter_types = flatten_parameter_types(event.arguments)
    for i in range(len(parameter_types)):
        parameter = LuaParameter(f"arg{i}")
        parameter.type = parameter_types[i]
        callback.parameters.append(parameter)
    converted_event.callback = callback

    if documentation is not None:
        converted_event.notes = documentation.notes

        doc_callback = documentation.callback
        if len(doc_callback.parameters) > len(callback.parameters):
            if error_handler is not None:
                error_handler.add_error(
                    RosettaMismatchError(event, documentation, "too_many_parameters"))
        elif len(doc_callback.parameters) < len(callback.parameters):
            if error_handler is not None:
                error_handler.add_error(
                    RosettaMismatchError(event, documentation, "not_enough_parameters"))
        else:
            for i in range(len(callback.parameters)):
                parameter = callback.parameters[i]
                parameter_documentation = doc_callback.parameters[i]
                if not is_compatible_type(parameter.type, parameter_documentation.type):
                    if error_handler is not None:
                        error_handler.add_error(
                            RosettaParameterTypeError(
                                event, documentation,
                                i, parameter.type, parameter_documentation.type
                            )
                        )
                else:
                    # only set documentation if the types match
                    parameter.name = parameter_documentation.name
                    parameter.notes = parameter_documentation.notes

    return converted_event
