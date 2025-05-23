import json

from .java.root import JavaRoot
from .root import RosettaRoot
from .game.projectzomboid.zomboid_root import ZomboidRoot
from .game.projectzomboid import zomboid_parser
from .java.parser import parse_root as parse_java

# TODO: this parser is not very robust: errors in the data are usually ignored


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

    if (languages := json_object.get("languages")) is not None and (java := languages.get("java")) is not None:
        if root.languages.get("java") is None:
            root.languages["java"] = JavaRoot()
        parse_java(root.languages["java"], java)

    return True
