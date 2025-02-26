from rosetta.object import RosettaObject
from ...lua.callback import LuaCallback
from .context import ZomboidContext


class ZomboidEvent(RosettaObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.deprecated: bool = False
        self.callback: LuaCallback | None = None
        self.context: ZomboidContext = ZomboidContext()
        self.tags: list[str] = []
