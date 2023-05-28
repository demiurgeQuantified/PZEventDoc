from generators import BaseGenerator, EmmyLuaGenerator, MarkdownGenerator
from PZEDGlobals import WantDeprecated


generators: dict = {
    "lua": EmmyLuaGenerator.EmmyLuaGenerator,
    "md": MarkdownGenerator.MarkdownGenerator,
}


def getGeneratorType(extension: str) -> [BaseGenerator.BaseGenerator]:
    try:
        return generators[extension]
    except KeyError:
        print("No generator found for extension ." + extension)
        return


def getGenerator(extension: str, wantDeprecated: WantDeprecated) -> [BaseGenerator.BaseGenerator]:
    generatorType = getGeneratorType(extension)
    if not generatorType:
        print("Failed to create generator")
        return

    return generatorType(wantDeprecated)
