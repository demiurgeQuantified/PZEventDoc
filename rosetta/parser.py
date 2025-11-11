import json

from pathlib import Path

try:
    import yaml
    from yamlcore import CoreLoader
except ImportError:
    yaml_present = False
else:
    yaml_present = True

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


def parse(root: RosettaRoot, object: dict) -> bool:
    if object.get("version") != "1.1":
        return False

    if (games := object.get("games")) is not None:
        parse_games(root.games, games)

    if (languages := object.get("languages")) is not None and (java := languages.get("java")) is not None:
        if root.languages.get("java") is None:
            root.languages["java"] = JavaRoot()
        parse_java(root.languages["java"], java)

    return True


def parse_json(root: RosettaRoot, str: str) -> bool:
    return parse(root, json.loads(str))


warned_yaml_missing = False


def parse_yaml(root: RosettaRoot, yml: str) -> bool:
    if not yaml_present:
        global warned_yaml_missing
        if not warned_yaml_missing:
            print("YML parsing requires PyYAML")
            warned_yaml_missing = True
        return False

    return parse(root, yaml.load(yml, CoreLoader))


def add(root: RosettaRoot, path: Path) -> None:
    if path.name.endswith(".json"):
        with path.open('r') as file:
            json = file.read()
        parse_json(root, json)
    elif path.name.endswith(".yml"):
        with path.open('r') as file:
            yml = file.read()
        parse_yaml(root, yml)
    else:
        raise ValueError("Unknown format for file at " + str(path))
