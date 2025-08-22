from rosetta.game.projectzomboid.event import ZomboidEvent
from rosetta.game.projectzomboid.zomboid_callback import ZomboidCallback
from rosetta.lua.callback import LuaCallback
from rosetta.object import RosettaObject
from rosetta.root import RosettaRoot

from .. import renderer_manager


class BaseRenderer:
    def __init__(self, name: str) -> None:
        """
        Base class for annotation generators

        :param name: Name of the format this renderer was registered under.
        :return:
        """
        super().__init__()
        self.render_deprecated: bool = False
        self.render_non_deprecated: bool = True
        self.rosetta: RosettaRoot | None = None

    def __init_subclass__(cls, names: list[str] = None, **kwargs):
        """

        :param names:
        :param kwargs:
        :return:
        """
        super().__init_subclass__(**kwargs)
        if names:
            renderer_manager.register_renderer(cls, names)

    def should_render(self, obj: RosettaObject) -> bool:
        """
        Returns true if the object should be rendered.

        :param obj: The object to check
        :return: Whether the object should be rendered
        """
        if obj.deprecated:
            if not self.render_deprecated:
                return False
        else:
            if not self.render_non_deprecated:
                return False

        return True

    @staticmethod
    def create_description(obj: RosettaObject) -> str:
        """
        Creates a description string for an object based on the passed properties

        :param obj: The event being described.
        :return:
        """
        description = ""
        if obj.name != "":
            description += f"{obj.name}: "
        if obj.notes != "":
            description += obj.notes

        if isinstance(obj, ZomboidEvent) or isinstance(obj, ZomboidCallback):
            if obj.context.multiplayer:
                if obj.context.client:
                    if not obj.context.server:
                        description = f"(Client) {description}"
                else:
                    description = f"(Server) {description}"

                if not obj.context.singleplayer:
                    description = f"(Multiplayer) {description}"
            else:
                description = f"(Singleplayer) {description}"

        if obj.deprecated:
            description = f"(Deprecated) {description}"

        return description

    def add_event(self, data: ZomboidEvent):
        """
        Writes documentation for an event

        :param data: Rosetta formatted event data
        :return:
        """
        raise NotImplementedError

    def add_hook(self, data: ZomboidEvent):
        """
        Writes documentation for a hook

        :param data: Rosetta formatted hook data
        :return:
        """
        raise NotImplementedError

    def add_callback(self, name: str, data: LuaCallback):
        """
        Writes documentation for a callback.

        :param name: Name of the callback
        :param data: Rosetta callback object
        :return:
        """
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError
