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
    def __init__(self, analysed: Event, rosetta: ZomboidEvent, index: int) -> None:
        super().__init__(analysed, rosetta, "parameter_type_mismatch")
        self.index: int = index


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
                real_type = error.analysed.arguments[0][error.index]
                rosetta_type = error.rosetta.callback.parameters[error.index].type
                print(f"Rosetta parameter type mismatch: {error.analysed.name}#{error.index}: "
                      f"got {rosetta_type}, expected {real_type}")


def convert_event(event: Event, documentation: ZomboidEvent | None = None,
                  error_handler: ErrorHandler | None = None) -> ZomboidEvent:
    converted_event = ZomboidEvent(event.name)

    callback = LuaCallback(f"umbrella.Callback_{event.name}")
    if len(event.arguments) > 0:
        for i in range(len(event.arguments[0])):
            parameter = LuaParameter(f"arg{i}")
            parameter.type = java_type_to_lua_type(event.arguments[0][i])
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
                if parameter.type != parameter_documentation.type:
                    if error_handler is not None:
                        error_handler.add_error(
                            RosettaParameterTypeError(event, documentation, i)
                        )
                else:
                    # only set documentation if the types match
                    parameter.name = parameter_documentation.name
                    parameter.notes = parameter_documentation.notes

    return converted_event
