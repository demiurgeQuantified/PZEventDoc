from ..object import RosettaObject
from .return_value import LuaReturn
from .parameter import LuaParameter


class LuaCallback(RosettaObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.parameters: list[LuaParameter] = []
        self.returns: list[LuaReturn] = []
        self.notes: str = ""
        self.tags: list[str] = []
