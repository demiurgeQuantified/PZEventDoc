from generators.BaseGenerator import BaseGenerator
from PZEDGlobals import WantDeprecated


class MarkdownGenerator(BaseGenerator, extensions=["md"]):
    # List of table names that have already been initialised
    initialisedTables: list[str]

    def __init__(self, wantDeprecated: WantDeprecated):
        """
        Class responsible for generating human-readable markdown documentation

        :param wantDeprecated: Deprecated object filtering configuration
        """
        BaseGenerator.__init__(self, wantDeprecated)
        self.initialisedTables = []

    @staticmethod
    def getParameterString(parameters: list[dict] = None) -> str:
        """
        Formats a string describing the parameters of a callback

        :param parameters: List of Rosetta formatted parameter objects
        :return:
        """
        result = ""
        if parameters is not None:
            for param in parameters:
                result += f"{param['name']} {param['type']}, "
        return result

    def initTable(self, name: str):
        """
        Creates a table heading

        :param name: Name of the table
        :return:
        """
        self.writeLine(f"# {name}")
        self.writeLine("Name | Description | Parameters")
        self.writeLine("--- | --- | ---")
        self.initialisedTables.append(name)

    def document(self, name: str, data: dict, tableType: str = "Events"):
        """
        Documents an event/hook

        :param name: Name of the event/hook
        :param data: Rosetta formatted event/hook object
        :param tableType: Name of the table (Events/Hook)
        :return:
        """
        deprecated: bool = data.get("deprecated", False)
        if not self.checkAllowDeprecated(deprecated):
            return

        if tableType not in self.initialisedTables:
            self.initTable(tableType)

        self.writeLine("{} | {} | {}".format(
            name,
            self.createDescription(data.get("notes", ""), deprecated, data.get("context")),
            self.getParameterString(data.get("callback"))
        ))

    def documentHook(self, name: str, data: dict):
        self.document(name, data, "Hook")

    def documentEvent(self, name: str, data: dict):
        self.document(name, data, "Events")
