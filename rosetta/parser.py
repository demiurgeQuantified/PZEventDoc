import json

from .root import RosettaRoot
from .game.projectzomboid.zomboid_root import ZomboidRoot
from .game.projectzomboid import zomboid_parser


def parse_games(games: dict[str, any], json_object: dict) -> bool:
    if (json_zomboid := json_object.get("projectzomboid")) is not None:
        if games.get("projectzomboid") is None:
            games["projectzomboid"] = ZomboidRoot()
        zomboid_parser.parse_zomboid(games["projectzomboid"], json_zomboid)

    return True


def parse_json(root: RosettaRoot, json_string: str) -> bool:
    json_object: dict = json.loads(json_string)
    if json_object.get("version") != "1.1":
        return False

    if (games := json_object.get("games")) is not None:
        parse_games(root.games, games)

    return True
