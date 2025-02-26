from rosetta.game.projectzomboid.context import ZomboidContext
from rosetta.lua.callback import LuaCallback


class ZomboidCallback(LuaCallback):
    def __init__(self, name: str):
        super().__init__(name)
        self.context: ZomboidContext = ZomboidContext()
