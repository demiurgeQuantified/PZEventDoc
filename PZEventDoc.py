# if my work helped you, please consider leaving me a tip ^u^
# https://ko-fi.com/starseamstress

import sys
import json
from getopt import getopt
from PZEDGlobals import *
import GeneratorManager
from generators import *


def loadOptions() -> tuple[str, str, WantDeprecated]:
    schemaFile: str = "data.json"
    outputFile: str = "Events.lua"
    wantDeprecated: WantDeprecated = WantDeprecated.NONE

    opts, _ = getopt(sys.argv[1:], 'dDs:o:')
    for option, argument in opts:
        if option == '-d':
            wantDeprecated = WantDeprecated.ALLOW
        elif option == '-D':
            wantDeprecated = WantDeprecated.EXCLUSIVE
        elif option == '-s':
            schemaFile = argument
        elif option == '-o':
            outputFile = argument

    return schemaFile, outputFile, wantDeprecated


def readJson(path: str) -> dict:
    """
    Reads a Json file as a dictionary

    :param path: The path of the file to read
    :return: Dictionary representing the file contents
    """
    file = open(path, 'r', encoding='utf-8')

    fileDict: dict
    try:
        fileDict = json.loads(file.read())
    finally:
        file.close()

    return fileDict


if __name__ == "__main__":
    schemaFile, outputFile, wantDeprecated = loadOptions()

    schema = readJson(schemaFile)
    if not schema:
        sys.exit(1)

    extension: str = outputFile.rsplit('.', 1)[1].lower()
    generator = GeneratorManager.getGenerator(extension, wantDeprecated)
    if not generator:
        sys.exit(2)

    generator.beginFile()

    events = schema.get("events")
    if events:
        for event in events:
            generator.documentEvent(event, events[event])

    hooks = schema.get("hooks")
    if hooks:
        for hook in hooks:
            generator.documentHook(hook, hooks[hook])

    if not generator.toFile(outputFile):
        sys.exit(3)
