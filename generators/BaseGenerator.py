from PZEDGlobals import WantDeprecated
import GeneratorManager


class BaseGenerator:
    def __init__(self, wantDeprecated: WantDeprecated):
        """
        Base class for annotation generators

        :param wantDeprecated: Deprecated object filtering configuration
        """
        self.totalString = ""
        self.wantDeprecated = wantDeprecated

    def __init_subclass__(cls, extensions: list[str] = None, **kwargs):
        """
        where does this show up?

        :param extensions:
        :param kwargs:
        :return:
        """
        super().__init_subclass__(**kwargs)
        if extensions:
            GeneratorManager.registerGenerator(cls, extensions)

    def writeLine(self, text: str):
        """
        Adds a line of text to the annotations

        :param text: The text to add
        :return:
        """
        self.totalString += f"{text}\n"

    def toFile(self, filepath: str):
        """
        Writes the stored annotations to a file

        :param filepath: The filepath to write to
        :return:
        """
        file = open(filepath, "w", encoding="utf-8")

        try:
            file.write(self.totalString)
        finally:
            file.close()

    def checkAllowDeprecated(self, deprecated: bool) -> bool:
        """
        Returns true if the current deprecated object rules allow this state to be annotated

        :param deprecated: If the object is deprecated
        :return: Whether the object should be annotated
        """
        if deprecated:
            if self.wantDeprecated == WantDeprecated.NONE:
                return False
        else:
            if self.wantDeprecated == WantDeprecated.EXCLUSIVE:
                return False

        return True

    @staticmethod
    def createDescription(name: str, notes: str = "", deprecated: bool = False, context: dict | None = None) -> str:
        """
        Creates a description string for an object based on the passed properties

        :param name: The display name of the object - may not be its actual code name
        :param notes: Notes about the object
        :param deprecated: Whether the object is deprecated
        :param context: The object's call contexts
        :return:
        """
        description = name + ": " + notes

        #  eugh
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

    def documentEvent(self, name: str, data: dict):
        """
        Writes documentation for an event

        :param name: Name of the event
        :param data: Rosetta formatted event data
        :return:
        """
        raise NotImplementedError

    def documentHook(self, name: str, data: dict):
        """
        Writes documentation for a hook

        :param name: Name of the hook
        :param data: Rosetta formatted hook data
        :return:
        """
        raise NotImplementedError

    def documentCallback(self, name: str, data: dict):
        """
        Writes documentation for a callback. Not all generators implement this.

        :param name: Name of the callback
        :param data: Rosetta callback object
        :return:
        """
        pass

    def get_final_string(self):
        raise NotImplementedError
