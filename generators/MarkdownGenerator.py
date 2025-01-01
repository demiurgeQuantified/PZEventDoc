import re

from generators.BaseGenerator import BaseGenerator
from PZEDGlobals import WantDeprecated


# TODO: allow the user to provide some kind of type resolver, so that these don't have to be hardcoded
TYPE_URLS: list[tuple[str, dict[str, str]]] = [
    ("https://demiurgequantified.github.io/ProjectZomboidJavaDocs/", {
        "IsoGameCharacter": "zombie/characters/IsoGameCharacter",
        "PerkFactory.Perk": "zombie/characters/skills/PerkFactory.Perk",
        "ObjectTooltip": "zombie/ui/ObjectTooltip/ObjectTooltip",
        "IsoGridSquare": "zombie/iso/IsoGridSquare",
        "State": "zombie/ai/State",
        "ChatMessage": "zombie/chat/ChatMessage",
        "IsoPlayer": "zombie/characters/IsoPlayer",
        "ClimateManager": "zombie/iso/weather/ClimateManager",
        "IsoLivingCharacter": "zombie/characters/IsoLivingCharacter",
        "SurvivorDesc": "zombie/characters/SurvivorDesc",
        "IsoSurvivor": "zombie/characters/IsoSurvivor",
        "IsoThumpable": "zombie/iso/objects/IsoThumpable",
        "WaveSignalDevice": "zombie/radio/devices/WaveSignalDevice",
        "MovableRecipe": "zombie/scripting/objects/MovableRecipe",
        "Moveable": "zombie/inventory/types/Moveable",
        "InventoryItem": "zombie/inventory/InventoryItem",
        "ItemContainer": "zombie/inventory/ItemContainer",
        "IsoObject": "zombie/iso/IsoObject",
        "DBResult": "zombie/network/DBResult",
        "IsoZombie": "zombie/characters/IsoZombie",
        "BodyPartType": "zombie/characters/BodyDamage/BodyPartType",
        "HandWeapon": "zombie/inventory/types/HandWeapon",
        "WeatherPeriod": "zombie/iso/weather/WeatherPeriod",
        "WeatherPeriod.WeatherStage": "zombie/iso/weather/WeatherPeriod.WeatherStage",
        "RecordedMedia": "zombie/radio/media/RecordedMedia",
        "ErosionSeason": "zombie/erosion/season/ErosionSeason",
        "IsoSpriteManager": "zombie/iso/sprite/IsoSpriteManager",
        "RadioScriptManager": "zombie/radio/scripting/RadioScriptManager",
        "BuildingDef": "zombie/iso/BuildingDef",
        "IsoFire": "zombie/iso/objects/IsoFire",
        "IsoMovingObject": "zombie/iso/IsoMovingObject",
        "IsoCell": "zombie/iso/IsoCell",
        "IsoRoom": "zombie/iso/areas/IsoRoom",
        "Server": "zombie/network/Server",
        "IsoTrap": "zombie/iso/objects/IsoTrap",
        "BaseVehicle": "zombie/vehicles/BaseVehicle",
        "Recipe": "zombie/scripting/objects/Recipe",
        "Recipe.Result": "zombie/scripting/objects/Recipe.Result",
        "Item": "zombie/scripting/objects/Item",
        "VehiclePart": "zombie/vehicles/VehiclePart",
        "IsoAnimal": "zombie/characters/animals/IsoAnimal",
        "IsoChunk": "zombie/iso/IsoChunk",
        "ContainerID": "zombie/network/fields/ContainerID",
        "IsoDeadBody": "zombie/iso/objects/IsoDeadBody",
        "AnimalTracks": "zombie/characters/animals/AnimalTracks",
        "CraftRecipeData": "zombie/entity/components/crafting/recipe/CraftRecipeData"
    }),
    ("https://docs.oracle.com/en/java/javase/17/docs/api/", {
        "ArrayList": "java.base/java/util/ArrayList",
        "Object": "java.base/java/lang/Object"
    })
]

if __debug__:
    missing_types: dict[str, True] = {}


def get_class_link(clazz: str) -> str | None:
    """
    Returns the link to a class's API page if it exists, else returns the input name

    :param clazz: The name of the class
    :return: Link to the class's API page or plain text name
    """
    for domain in TYPE_URLS:
        url = domain[1].get(clazz)
        if url is not None:
            return f"{domain[0]}{url}.html"

    if __debug__:
        if missing_types.get(clazz) is None:
            print("(DEBUG) No link defined for type " + clazz)
            missing_types[clazz] = True


TYPE_SUFFIXES: list[str] = ["[]", "?"]


def get_formatted_type(type_name: str) -> str:
    generic_match = re.search("(.+?)<(.+)>", type_name)
    if generic_match is not None:
        type_names = generic_match.group(2).split(",")
        formatted_names = ""
        do_comma = False
        for type_name in type_names:
            if do_comma:
                formatted_names += ", "
            formatted_names += get_formatted_type(type_name.strip())
            do_comma = True
        return f"{get_formatted_type(generic_match.group(1))}<{formatted_names}>"
    else:
        first_suffix_pos: int = len(type_name)
        for suffix in TYPE_SUFFIXES:
            suffix_pos = type_name.rfind(suffix)
            if suffix_pos != -1 and suffix_pos < first_suffix_pos:
                first_suffix_pos = suffix_pos
        internal_type_name = type_name[:first_suffix_pos]
        suffixes = type_name[first_suffix_pos:]

        link = get_class_link(internal_type_name)
        if link is not None:
            return f"[{internal_type_name}]({link}){suffixes}"
        else:
            return type_name


def get_formatted_type_union(type_name: str) -> str:
    types: list[str] = type_name.split('|')

    result_str = ""
    do_or = False
    num_lines = 1
    for type_name in types:
        formatted_type = get_formatted_type(type_name)
        if do_or:
            result_str += " or "
            if len(result_str) + len(formatted_type) > 40 * num_lines:
                result_str += "<br>"
                num_lines += 1
        result_str += formatted_type

        do_or = True

    return result_str


class MarkdownGenerator(BaseGenerator, extensions=["md"]):

    def __init__(self, wantDeprecated: WantDeprecated):
        """
        Class responsible for generating human-readable markdown documentation

        :param wantDeprecated: Deprecated object filtering configuration
        """
        BaseGenerator.__init__(self, wantDeprecated)

        # documentation is stored separately for each heading, so that the document functions can be called out of order
        # without the end result becoming mixed
        self.headings: dict[str, str] = {}

    def toFile(self, filepath: str):
        self.finalise()
        BaseGenerator.toFile(self, filepath)

    def finalise(self):
        """
        Turns the per-heading strings into a single string to write to file
        :return:
        """
        for heading, totalStr in self.headings.items():
            self.writeLine("# " + heading)
            self.writeLine(totalStr)

    @staticmethod
    def createTable(columnHeadings: list[str], rows: list[list[str]]) -> str:
        """
        Creates and returns a markdown table with the provided table

        :param columnHeadings: The string headings of the table columns
        :param rows: List of lists of strings. Each sub-list will become a row in the table.
        All rows should be the same length as columnHeadings
        :return: The table
        """
        assert len(columnHeadings) > 0, "Markdown: createTable: Table has zero columns"
        headings = "|"
        divider = "|"
        for heading in columnHeadings:
            headings += f" {heading} |"
            divider += " --- |"

        result: str = headings + "\n" + divider + "\n"

        for row in rows:
            assert len(row) == len(columnHeadings), \
                f"Markdown: createTable: row has {len(row)} entries in {len(columnHeadings)} column table"
            result += "|"
            for item in row:
                item = item.replace('|', '\\|')
                result += f" {item} |"
            result += "\n"
        return result

    def createCallbackDoc(self, data: dict) -> str:
        """
        Creates and returns documentation for the parameters and return value of a callback.
        If there are no parameters an empty parameters section will be created.
        If there is no return value no returns section will be created.

        :param data: Callback definition
        :return: Callback documentation
        """
        result = "\n**Parameters**\n\n"

        if len(data["parameters"]) > 0:
            paramDetails: list[list[str]] = []
            for parameter in data["parameters"]:
                paramDetails.append([parameter["name"], get_formatted_type_union(parameter["type"]), parameter.get("notes", "")])

            result += self.createTable(["Name", "Type", "Notes"], paramDetails)
        else:
            result += "None.\n"

        retVal = data.get("returns")
        if retVal:
            result += "\n**Returns**\n\n"
            result += self.createTable(["Name", "Type", "Notes"],
                                       [[retVal.get("name", ""), retVal["type"], retVal.get("notes", "")]])

        return result

    def document(self, name: str, data: dict, callback: dict, heading: str = "Events"):
        """
        Documents an object

        :param name: Name of the event/hook
        :param data: Rosetta formatted event/hook object
        :param callback: Callback definition
        :param heading: Heading under which to place the object (Events/Hook)
        :return:
        """
        deprecated: bool = data.get("deprecated", False)
        if not self.checkAllowDeprecated(deprecated):
            return

        totalStr = "## " + name + "\n"
        totalStr += self.createDescription(data.get("name", name), data.get("notes", ""), deprecated, data.get("context")) + "\n"

        totalStr += self.createCallbackDoc(callback)

        if not self.headings.get(heading):
            self.headings[heading] = ""
        self.headings[heading] += totalStr

    def documentHook(self, name: str, data: dict):
        self.document(name, data, data["callback"], "Hook")

    def documentEvent(self, name: str, data: dict):
        callback = data.get("callback")
        if not callback:
            return
        self.document(name, data, callback, "Events")

    def documentCallback(self, name: str, data: dict):
        # kinda scuffed...
        self.document(name, data, data, "Callbacks")

    def get_final_string(self):
        self.finalise()
        return self.totalString
