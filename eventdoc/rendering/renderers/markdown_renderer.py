import re
import typing

from eventdoc.rendering.renderers.base_renderer import BaseRenderer
from rosetta.game.projectzomboid.event import ZomboidEvent
from rosetta.java.root import JavaRoot
from rosetta.lua.callback import LuaCallback

# most urls can be resolved from rosetta now, but keeping these here until the update action is updated to use rosetta
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
        "CraftRecipeData": "zombie/entity/components/crafting/recipe/CraftRecipeData",
        "DBBannedIP": "network/DBBannedIP"
    }),
    ("https://docs.oracle.com/en/java/javase/17/docs/api/", {
        "ArrayList": "java.base/java/util/ArrayList",
        "Object": "java.base/java/lang/Object"
    })
]

JAVADOCS_URL: str = "https://demiurgequantified.github.io/ProjectZomboidJavaDocs/"

if __debug__:
    missing_types: set[str] = set()


TYPE_SUFFIXES: list[str] = ["[]", "?"]


class MarkdownRenderer(BaseRenderer, names=["md"]):
    def __init__(self, name: str):
        """
        Class responsible for generating human-readable markdown documentation
        """
        super().__init__(name)

        # documentation is stored separately for each heading, so that the document functions can be called out of order
        # without the end result becoming mixed
        self.headings: dict[str, str] = {}

    def get_class_link(self, clazz: str) -> str | None:
        """
        Returns the link to a class's API page if it exists, else returns the input name

        :param clazz: The name of the class
        :return: Link to the class's API page or plain text name
        """
        if clazz.startswith("umbrella."):
            return f"https://github.com/demiurgeQuantified/PZEventDoc/blob/develop/extra.lua"

        # TODO: this sucks!!! this is so slow!!
        java = self.rosetta.languages.get("java")
        if java is not None:
            java = typing.cast(JavaRoot, java)
            for name, package in java.packages.items():
                for type in package.types:
                    if type.name == clazz:
                        return JAVADOCS_URL + "/" + package.name.replace(".", "/") + "/" + clazz + ".html"

        for domain in TYPE_URLS:
            url = domain[1].get(clazz)
            if url is not None:
                return f"{domain[0]}{url}.html"

        if __debug__:
            if clazz not in missing_types:
                print("(DEBUG) No link defined for type " + clazz)
                missing_types.add(clazz)

    def get_formatted_type(self, type_name: str) -> str:
        generic_match = re.search("(.+?)<(.+)>", type_name)
        if generic_match is not None:
            type_names = generic_match.group(2).split(",")
            formatted_names = ""
            do_comma = False
            for type_name in type_names:
                if do_comma:
                    formatted_names += ", "
                formatted_names += self.get_formatted_type(type_name.strip())
                do_comma = True
            return f"{self.get_formatted_type(generic_match.group(1))}<{formatted_names}>"
        else:
            first_suffix_pos: int = len(type_name)
            for suffix in TYPE_SUFFIXES:
                suffix_pos = type_name.rfind(suffix)
                if suffix_pos != -1 and suffix_pos < first_suffix_pos:
                    first_suffix_pos = suffix_pos
            internal_type_name = type_name[:first_suffix_pos]
            suffixes = type_name[first_suffix_pos:]

            link = self.get_class_link(internal_type_name)
            if link is not None:
                return f"[{internal_type_name}]({link}){suffixes}"
            else:
                return type_name

    def get_formatted_type_union(self, type_name: str) -> str:
        types: list[str] = list(type.strip() for type in type_name.split('|'))

        result_str = ""
        do_or = False
        num_lines = 1
        for type_name in types:
            formatted_type = self.get_formatted_type(type_name)
            if do_or:
                result_str += " or "
                if len(result_str) + len(formatted_type) > 40 * num_lines:
                    result_str += "<br>"
                    num_lines += 1
            result_str += formatted_type

            do_or = True

        return result_str

    @staticmethod
    def create_table(headings: list[str], rows: list[list[str]]) -> str:
        """
        Creates and returns a Markdown table with the provided table

        :param headings: The string headings of the table columns
        :param rows: List of lists of strings. Each sub-list will become a row in the table.
        All rows should be the same length as columnHeadings
        :return: The table
        """
        assert len(headings) > 0, "Table has zero columns"
        heading_string = "|"
        divider = "|"
        for heading in headings:
            heading_string += f" {heading} |"
            divider += " --- |"

        result: str = heading_string + "\n" + divider + "\n"

        for row in rows:
            assert len(row) == len(headings), \
                f"Row has {len(row)} entries in {len(headings)} column table"
            result += "|"
            for item in row:
                item = item.replace('|', '\\|')
                result += f" {item} |"
            result += "\n"
        return result

    def create_callback_doc(self, data: LuaCallback) -> str:
        """
        Creates and returns documentation for the parameters and return value of a callback.
        If there are no parameters an empty parameters section will be created.
        If there is no return value no returns section will be created.

        :param data: Callback definition
        :return: Callback documentation
        """
        result = "\n**Parameters**\n\n"

        if len(data.parameters) > 0:
            parameter_details: list[list[str]] = []
            for parameter in data.parameters:
                parameter_details.append(
                    [parameter.name, self.get_formatted_type_union(parameter.type), parameter.notes])

            result += self.create_table(["Name", "Type", "Notes"], parameter_details)
        else:
            result += "None.\n"

        if len(data.returns) > 0:
            result += "\n**Returns**\n\n"
            returns_details: list[list[str]] = []
            for retval in data.returns:
                returns_details.append(
                    [retval.name, self.get_formatted_type_union(retval.type), retval.notes])

            result += self.create_table(["Name", "Type", "Notes"], returns_details)

        return result

    def document(self, data: ZomboidEvent, heading: str):
        """
        Documents an object

        :param data: Rosetta formatted event/hook object
        :param heading: Heading under which to place the object (Events/Hook)
        :return:
        """
        if not self.should_render(data):
            return

        total_str = "## " + data.name + "\n"
        total_str += self.create_description(data) + "\n"

        total_str += self.create_callback_doc(data.callback)

        if not self.headings.get(heading):
            self.headings[heading] = ""
        self.headings[heading] += total_str

    def add_hook(self, data: ZomboidEvent):
        self.document(data, "Hooks")

    def add_event(self, data: ZomboidEvent):
        self.document(data, "Events")

    def add_callback(self, name: str, data: LuaCallback):
        total_str = "## " + name + "\n"
        total_str += self.create_description(data) + "\n"

        total_str += self.create_callback_doc(data)

        if not self.headings.get("Callbacks"):
            self.headings["Callbacks"] = ""
        self.headings["Callbacks"] += total_str

    def render(self):
        full_string = ""
        for heading, text in self.headings.items():
            full_string += f"# {heading}\n{text}"
        return full_string
