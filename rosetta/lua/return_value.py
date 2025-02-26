from ..object import RosettaObject


class LuaReturn(RosettaObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.type: str = ""
        self.nullable: bool = False
