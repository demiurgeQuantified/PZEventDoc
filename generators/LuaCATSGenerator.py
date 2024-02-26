from generators.BaseGenerator import BaseGenerator
from PZEDGlobals import WantDeprecated


fileOpener: str = """---@meta
-- Generated by PZEventDoc https://github.com/demiurgeQuantified/PZEventDoc

-- If it helped you, please consider leaving me a tip ^u^
-- https://ko-fi.com/starseamstress\n
"""


class LuaCATSGenerator(BaseGenerator, extensions=["lua"]):
    # List of table names that have already been initialised
    initialisedTables: list[str]
    # The current level of indentation
    currentIndentation: int

    def __init__(self, wantDeprecated: WantDeprecated):
        """
        Class responsible for generating LuaCATS annotations

        :param wantDeprecated: Defines how deprecated objects should be treated
        """
        BaseGenerator.__init__(self, wantDeprecated)
        self.initialisedTables = []
        self.currentIndentation = 0

    def writeLine(self, text: str):
        """
        Writes a line with the current level of indentation

        :param text: The text to write
        :return:
        """
        self.totalString += "    " * self.currentIndentation + f"{text}\n"

    def beginFile(self):
        """
        Adds the opening metadata to the file

        :return:
        """
        self.totalString = fileOpener

    @staticmethod
    def getFunctionSignature(params: list[dict[str, str]] = None) -> str:
        """
        Returns a function signature type description

        :param params: List of Rosetta formatted parameter definitions
        :return:
        """
        if params is None or len(params) == 0:
            return "function"

        formattedParams = ""
        doComma = False
        for parameter in params:
            if doComma:
                formattedParams += ","
            else:
                doComma = True

            formattedParams += f"{parameter['name']}:{parameter['type']}"

        return f"fun({formattedParams}):any"

    @staticmethod
    def formatFunction(name: str, args: list[str] = None) -> str:
        """
        Returns an empty function declaration

        :param name: Name of the function to declare
        :param args: List of parameter names
        :return:
        """
        formattedArgs = ""
        if not (args is None or len(args) == 0):
            formattedArgs = args[0]
            for label in args[1:]:
                formattedArgs += f", {label}"

        return f"{name} = function({formattedArgs}) end,"

    def documentFunction(self, name: str, callbackType: str):
        """
        Documents a function that takes a single callback argument

        :param name: Name of the function
        :param callbackType: Name of the callback type
        :return:
        """
        self.writeLine("---@param callback " + callbackType)

        self.writeLine(self.formatFunction(name, ["callback"]))

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

        if deprecated:
            self.writeLine("---@deprecated")

        callbackType = "Callback_" + name
        self.writeLine(f"---@alias {callbackType} {self.getFunctionSignature(data.get('callback'))}\n")

        self.writeLine("---" + self.getDescription(data.get("notes", ""), deprecated, data.get("context", {})))
        self.writeLine(f"{tableName}.{name} = {{")
        self.currentIndentation += 1

        self.documentFunction("Add", callbackType)
        self.documentFunction("Remove", callbackType)

        self.currentIndentation -= 1
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