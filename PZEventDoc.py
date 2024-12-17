# if my work helped you, please consider leaving me a tip ^u^
# https://ko-fi.com/starseamstress

import sys
import json
from getopt import getopt
from PZEDGlobals import *
import GeneratorManager
from generators import *


# TODO: some kind of object would be prettier than this tuple
def loadOptions() -> tuple[str, str, WantDeprecated, bool, bool, bool]:
    """
    Returns a tuple containing options passed at the command line

    :return: input filepath, output filepath, wantDeprecated, wantEvents, wantHooks, wantCallbacks
    """
    dataFile: str = "data.json"
    outputFile: str = "Events.lua"
    wantDeprecated: WantDeprecated = WantDeprecated.NONE
    wantEvents = False
    wantHooks = False
    wantCallbacks = False

    opts, _ = getopt(sys.argv[1:], 'dDs:o:')
    for option, argument in opts:
        if option == '-d':
            wantDeprecated = WantDeprecated.ALLOW
        elif option == '-D':
            wantDeprecated = WantDeprecated.EXCLUSIVE
        elif option == '-s':
            dataFile = argument
        elif option == '-o':
            outputFile = argument
        elif option == '-e':
            wantEvents = True
        elif option == '-h':
            wantHooks = True
        elif option == '-c':
            wantCallbacks = True

    # default behaviour: if no table flags are set, all types are enabled
    if not wantEvents and not wantHooks and not wantCallbacks:
        wantEvents = True
        wantHooks = True
        wantCallbacks = True

    return dataFile, outputFile, wantDeprecated, wantEvents, wantHooks, wantCallbacks


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
    dataFile, outputFile, wantDeprecated, wantEvents, wantHooks, wantCallbacks = loadOptions()

    data = readJson(dataFile)

    extension: str = outputFile.rsplit('.', 1)[1].lower()
    generator = GeneratorManager.getGenerator(extension, wantDeprecated)

    if wantEvents:
        events: dict = data.get("events")
        if events:
            for name, event in events.items():
                generator.documentEvent(name, event)

    if wantHooks:
        hooks: dict = data.get("hooks")
        if hooks:
            for name, hook in hooks.items():
                generator.documentHook(name, hook)

    if wantCallbacks:
        callbacks: dict = data.get("callbacks")
        if callbacks:
            for name, callback in callbacks.items():
                generator.documentCallback(name, callback)

    generator.toFile(outputFile)
