from PZEDGlobals import WantDeprecated


class BaseGenerator:
    def __init__(self, wantDeprecated: WantDeprecated):
        self.totalString = ""
        self.wantDeprecated = wantDeprecated

    def beginFile(self):
        self.totalString = ""

    def writeLine(self, text: str):
        self.totalString += f"{text}\n"

    def toFile(self, outputFile: str) -> bool:
        try:
            file = open(outputFile, "w", encoding="utf-8")
        except OSError:
            print(f"ERROR: Failed to open {outputFile}")
            return False

        file.write(self.totalString)
        file.close()
        return True

    def checkAllowDeprecated(self, deprecated: bool) -> bool:
        if deprecated:
            if self.wantDeprecated == WantDeprecated.NONE:
                return False
        else:
            if self.wantDeprecated == WantDeprecated.EXCLUSIVE:
                return False

        return True

    @staticmethod
    def getDescription(description: str = "", deprecated: bool = False, context: dict | None = None) -> str:
        if context is not None:
            if context.get("multiplayer", True):
                if context.get("client", True):
                    if not context.get("server", True):
                        description = f"(Client) {description}"
                else:
                    description = f"(Server) {description}"

                if not context.get("singleplayer", True):
                    description = f"(Multiplayer) {description}"
            else:
                description = f"(Singleplayer) {description}"

        if deprecated:
            description = f"(Deprecated) {description}"

        return description

    def documentEvent(self, name, data):
        print(f"ERROR: {self.__class__.__name__} is missing documentEvent")

    def documentHook(self, name, data):
        print(f"ERROR: {self.__class__.__name__} is missing documentHook")

