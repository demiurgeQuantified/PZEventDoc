from PZEDGlobals import WantDeprecated


class BaseGenerator:
    def __init__(self, wantDeprecated: WantDeprecated):
        self.totalString = ""
        self.wantDeprecated = wantDeprecated

    def beginFile(self):
        self.totalString = ""

    def toFile(self, outputFile: str) -> bool:
        try:
            file = open(outputFile, "w", encoding="utf-8")
        except OSError:
            print("ERROR: Failed to open " + outputFile)
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
    def getDescription(description="", deprecated=False, context={}) -> str:
        if context.get("multiplayer", True):
            if context.get("client", True):
                if not context.get("server", True):
                    description = "(Client) " + description
            else:
                description = "(Server) " + description

            if not context.get("singleplayer", True):
                description = "(Multiplayer) " + description
        else:
            description = "(Singleplayer) " + description

        if deprecated:
            description = "(Deprecated) " + description

        return description

    def documentEvent(self, name, data):
        print("ERROR: " + self.__class__.__name__ + " is missing documentEvent")

    def documentHook(self, name, data):
        print("ERROR: " + self.__class__.__name__ + " is missing documentHook")

