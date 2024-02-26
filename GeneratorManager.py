from PZEDGlobals import WantDeprecated

from typing import TYPE_CHECKING, Type
if TYPE_CHECKING:
    from generators.BaseGenerator import BaseGenerator


generators: dict[str, Type["BaseGenerator"]] = {}


def getGeneratorType(extension: str) -> Type["BaseGenerator"]:
    try:
        return generators[extension]
    except KeyError:
        raise Exception("No generator found for extension ." + extension)


def getGenerator(extension: str, wantDeprecated: WantDeprecated) -> "BaseGenerator":
    generatorType = getGeneratorType(extension)
    if not generatorType:
        raise Exception("Failed to create generator")

    return generatorType(wantDeprecated)


def registerGenerator(generatorType: Type["BaseGenerator"], extensions: list[str]):
    """
    Registers a class as the generator for a file extension

    :param generatorType: The class to handle these extensions with
    :param extensions: List of file extensions to register this generator for
    :return:
    """
    for extension in extensions:
        generators[extension] = generatorType
