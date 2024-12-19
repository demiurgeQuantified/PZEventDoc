from generators.BaseGenerator import BaseGenerator
from PZEDGlobals import WantDeprecated
import pathlib


class LuaCATSGenerator(BaseGenerator, extensions=["lua"]):
    initialisedTables: list[str]
    """List of table names that have already been initialised"""
    current_indentation: int
    """The current level of indentation"""

    def __init__(self, wantDeprecated: WantDeprecated):
        """
        Class responsible for generating LuaCATS annotations

        :param wantDeprecated: Defines how deprecated objects should be treated
        """
        BaseGenerator.__init__(self, wantDeprecated)
        self.initialisedTables = []
        self.current_indentation = 0

        path = pathlib.Path(__file__).parent.parent / "extra.lua"
        file = path.open('r')
        self.totalString = file.read() + "\n"
        file.close()

    def writeLine(self, text: str):
        """
        Writes a line with the current level of indentation

        :param text: The text to write
        :return:
        """
        self.totalString += "    " * self.current_indentation + f"{text}\n"

    @staticmethod
    def get_function_signature(data: dict) -> str:
        """
        Returns a function signature type description

        :param data: Rosetta callback definition
        :return:
        """
        signature = "fun("

        params = data.get("parameters")
        returns = data.get("returns")
        if params and len(params) != 0:
            do_comma = False
            for parameter in params:
                if do_comma:
                    signature += ","
                else:
                    do_comma = True

                # TODO: if parameter types were processed into objects with specialisations as properties this would be much simpler

                parameter_type: str = parameter['type']
                # remove non-table generics
                if parameter_type.find("<") and not (parameter_type.startswith("table")):
                    parameter_type = parameter_type.split("<", 1)[0]

                signature += f"{parameter['name']}:{parameter_type}"
        elif not returns:  # callback has no parameters or return type
            return "function"
        signature += ")"

        if returns:
            signature += ":"
            name: str = returns.get("name")
            if name:
                signature += f"{name}:"
            signature += returns["type"]

        return signature

    @staticmethod
    def getCallbackDescription(callback: dict) -> str:
        description = ""

        notes: str = callback.get("notes")
        if notes:
            description = notes + "<br><br>"

        params: list[dict] = callback.get("parameters")
        if params:
            for param in params:
                notes: str = param.get("notes")
                if not notes:
                    continue
                description = description + f"{param['name']} - {notes}<br>"

        returnValue: dict = callback.get("returns")
        if returnValue:
            name = returnValue.get("name")
            if name:
                description = description + f"<br>Returns: {name}"
                notes: str = returnValue.get("notes")
                if notes:
                    description = description + f" - {notes}"

        return description

    @staticmethod
    def formatFunction(name: str, args: list[str]) -> str:
        """
        Returns an empty function declaration

        :param name: Name of the function to declare
        :param args: List of parameter names
        :return:
        """
        formatted_args = ""
        if not (len(args) == 0):
            formatted_args = args[0]
            for label in args[1:]:
                formatted_args += f", {label}"

        return f"{name} = function({formatted_args}) end,"

    def documentFunction(self, name: str, callbackType: str):
        """
        Documents a function that takes a single callback argument

        :param name: Name of the function
        :param callbackType: Name of the callback type
        :return:
        """
        self.writeLine("---@param callback " + callbackType)

        self.writeLine(self.formatFunction(name, ["callback"]))

    def documentType(self, name: str, data: dict):
        """
        Documents a function type

        :param name: Name of the type
        :param data: Rosetta formatted list of parameters
        :return:
        """
        self.writeLine("---" + self.getCallbackDescription(data))
        self.writeLine(f"---@alias {name} {self.get_function_signature(data)}\n")

    def initTable(self, name: str):
        """
        Initialises an empty lua table

        :param name: Name of the table
        :return:
        """
        self.writeLine(name + " = {}\n")
        self.initialisedTables.append(name)

    def document(self, name: str, data: dict, tableName: str = "Events"):
        """
        Documents an event/hook's callback type and Add/Remove functions

        :param name: Name of the event/hook
        :param data: Rosetta formatted event/hook data
        :param tableName: Name of the table containing the object (Events/Hook)
        :return:
        """
        deprecated: bool = data.get("deprecated", False)
        if not self.checkAllowDeprecated(deprecated):
            return

        if tableName not in self.initialisedTables:
            self.initTable(tableName)

        callback = data.get("callback")
        if callback is not None:
            callback_type = "Callback_" + name
            self.documentType(callback_type, callback)
        else:
            callback_type = "function"

        if deprecated:
            self.writeLine("---@deprecated")

        self.writeLine("---" + self.createDescription(
            data.get("name", name), data.get("notes", ""), deprecated, data.get("context", {})))
        if callback_type != "function":
            self.writeLine("---<br><br>" + self.getCallbackDescription(data['callback']))

        self.writeLine(f"{tableName}.{name} = {{")
        self.current_indentation += 1

        self.documentFunction("Add", callback_type)
        self.documentFunction("Remove", callback_type)

        self.current_indentation -= 1
        self.writeLine("}\n")

    def documentHook(self, name: str, data: dict):
        """
        Writes documentation for a hook

        :param name: Name of the hook
        :param data: Rosetta formatted hook data
        :return:
        """
        self.document(name, data, "Hook")

    def documentEvent(self, name: str, data: dict):
        """
        Writes documentation for an event

        :param name: Name of the event
        :param data: Rosetta formatted event data
        :return:
        """
        self.document(name, data, "Events")

    def documentCallback(self, name: str, data: dict):
        """
        Writes documentation for a callback

        :param name: Name of the callback
        :param data: Rosetta callback object
        :return:
        """
        self.documentType(name, data)

    def get_final_string(self):
        return self.totalString
