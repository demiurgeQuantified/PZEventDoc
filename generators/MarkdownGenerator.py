from generators.BaseGenerator import BaseGenerator
from PZEDGlobals import WantDeprecated


class MarkdownGenerator(BaseGenerator, extensions=["md"]):

    def __init__(self, wantDeprecated: WantDeprecated):
        """
        Class responsible for generating human-readable markdown documentation

        :param wantDeprecated: Deprecated object filtering configuration
        """
        BaseGenerator.__init__(self, wantDeprecated)

        # documentation is stored separately for each heading, so that the document functions can be called out of order
        # without the end result becoming mixed
        self.headings: dict[str, str] = {}

    def toFile(self, filepath: str):
        self.finalise()
        BaseGenerator.toFile(self, filepath)

    def finalise(self):
        """
        Turns the per-heading strings into a single string to write to file
        :return:
        """
        for heading, totalStr in self.headings.items():
            self.writeLine("# " + heading)
            self.writeLine(totalStr)

    @staticmethod
    def createTable(columnHeadings: list[str], rows: list[list[str]]) -> str:
        """
        Creates and returns a markdown table with the provided table

        :param columnHeadings: The string headings of the table columns
        :param rows: List of lists of strings. Each sub-list will become a row in the table.
        All rows should be the same length as columnHeadings
        :return: The table
        """
        assert len(columnHeadings) > 0, "Markdown: createTable: Table has zero columns"
        headings = "|"
        divider = "|"
        for heading in columnHeadings:
            headings += f" {heading} |"
            divider += " --- |"

        result: str = headings + "\n" + divider + "\n"

        for row in rows:
            assert len(row) == len(columnHeadings),\
                f"Markdown: createTable: row has {len(row)} entries in {len(columnHeadings)} column table"
            result += "|"
            for item in row:
                result += f" {item} |"
            result += "\n"
        return result

    def createCallbackDoc(self, data: dict) -> str:
        """
        Creates and returns documentation for the parameters and return value of a callback.
        If there are no parameters an empty parameters section will be created.
        If there is no return value no returns section will be created.

        :param data: Callback definition
        :return: Callback documentation
        """
        result = "### Parameters\n"

        if len(data["parameters"]) > 0:
            paramDetails: list[list[str]] = []
            for parameter in data["parameters"]:
                paramDetails.append([parameter["name"], parameter["type"], parameter.get("notes", "")])

            result += self.createTable(["Name", "Type", "Notes"], paramDetails)
        else:
            result += "None.\n"

        retVal = data.get("returns")
        if retVal:
            result += "### Returns\n"
            result += self.createTable(["Name", "Type", "Notes"],
                                       [[retVal.get("name", ""), retVal["type"], retVal.get("notes", "")]])

        return result

    def document(self, name: str, data: dict, callback: dict, heading: str = "Events"):
        """
        Documents an object

        :param name: Name of the event/hook
        :param data: Rosetta formatted event/hook object
        :param data: Callback definition
        :param heading: Heading under which to place the object (Events/Hook)
        :return:
        """
        deprecated: bool = data.get("deprecated", False)
        if not self.checkAllowDeprecated(deprecated):
            return

        totalStr = "## " + name + "\n"
        totalStr += self.createDescription(data.get("name", name), data.get("notes", ""), deprecated, data.get("context")) + "\n"

        totalStr += self.createCallbackDoc(callback)

        if not self.headings.get(heading):
            self.headings[heading] = ""
        self.headings[heading] += totalStr

    def documentHook(self, name: str, data: dict):
        self.document(name, data, data["callback"], "Hook")

    def documentEvent(self, name: str, data: dict):
        self.document(name, data, data["callback"], "Events")

    def documentCallback(self, name: str, data: dict):
        # kinda scuffed...
        self.document(name, data, data, "Callbacks")
