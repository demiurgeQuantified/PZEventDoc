from generators.BaseGenerator import BaseGenerator


class MarkdownGenerator(BaseGenerator, extensions=["md"]):
    def __init__(self, wantDeprecated):
        BaseGenerator.__init__(self, wantDeprecated)
        self.initialisedTables = []

    @staticmethod
    def getParameterString(parameters: list[dict] = None) -> str:
        result = ""
        if parameters is not None:
            for param in parameters:
                result += f"{param['name']} {param['type']}, "
        return result

    def initTable(self, name: str):
        self.writeLine(f"# {name}")
        self.writeLine("Name | Description | Parameters")
        self.writeLine("--- | --- | ---")
        self.initialisedTables.append(name)

    def document(self, name: str, data: dict, tableType: str = "Events"):
        deprecated: bool = data.get("deprecated", False)
        if not self.checkAllowDeprecated(deprecated):
            return

        if tableType not in self.initialisedTables:
            self.initTable(tableType)

        self.writeLine("{} | {} | {}".format(
            name,
            self.getDescription(data.get("notes", ""), deprecated, data.get("context")),
            self.getParameterString(data.get("callback"))
        ))

    def documentHook(self, name: str, data: dict):
        self.document(name, data, "Hook")

    def documentEvent(self, name: str, data: dict):
        self.document(name, data, "Events")
