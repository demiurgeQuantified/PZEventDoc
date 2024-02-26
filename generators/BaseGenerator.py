from PZEDGlobals import WantDeprecated
import GeneratorManager


class BaseGenerator:
    def __init__(self, wantDeprecated: WantDeprecated):
        self.totalString = ""
        self.wantDeprecated = wantDeprecated

    def __init_subclass__(cls, extensions: list[str] = None, **kwargs):
        super().__init_subclass__(**kwargs)
        if extensions:
            GeneratorManager.registerGenerator(cls, extensions)

    def beginFile(self):
        self.totalString = ""

    def writeLine(self, text: str):
        self.totalString += f"{text}\n"

    def toFile(self, outputFile: str):
        file = open(outputFile, "w", encoding="utf-8")

        try:
            file.write(self.totalString)
        finally:
            file.close()

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
        raise NotImplementedError

    def documentHook(self, name, data):
        raise NotImplementedError

