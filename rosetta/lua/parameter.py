from ..object import RosettaObject


class LuaParameter(RosettaObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.type: str = ""
        self.optional: bool = False
        self.nullable: bool = False
