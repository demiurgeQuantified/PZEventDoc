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
    try:
        dataFile, outputFile, wantDeprecated = loadOptions()

        try:
            data = readJson(dataFile)
        except Exception as e:
            print("Error opening input file: " + str(e))
            raise e

        extension: str = outputFile.rsplit('.', 1)[1].lower()
        generator = GeneratorManager.getGenerator(extension, wantDeprecated)

        generator.beginFile()

        events = data.get("events")
        if events:
            for event in events:
                generator.documentEvent(event, events[event])

        hooks = data.get("hooks")
        if hooks:
            for hook in hooks:
                generator.documentHook(hook, hooks[hook])

        try:
            generator.toFile(outputFile)
        except Exception as e:
            raise Exception("Error writing output file: " + str(e))
    except Exception as e:
        print("Annotation generation failed: " + str(e))