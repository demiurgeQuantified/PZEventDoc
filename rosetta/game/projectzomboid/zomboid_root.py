from rosetta.game.projectzomboid.event import ZomboidEvent
from rosetta.lua.callback import LuaCallback


class ZomboidRoot:
    def __init__(self):
        self.events: list[ZomboidEvent] = []
        self.hooks: list[ZomboidEvent] = []
        self.callbacks: dict[str, LuaCallback] = {}
