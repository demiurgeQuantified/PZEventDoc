# if my work helped you, please consider leaving me a tip ^u^
# https://ko-fi.com/starseamstress

import sys
import json
from getopt import getopt
from PZEDGlobals import *
import GeneratorManager


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


def loadJson(filename: str) -> dict | None:
    try:
        file = open(filename, 'r', encoding='utf-8')
    except OSError:
        print(f"ERROR: Failed to open {filename}")
        return

    fileDict: dict | None = None
    try:
        fileDict = json.loads(file.read())
    except json.JSONDecodeError:
        print(f"ERROR: {filename} is not a valid JSON file.")
    finally:
        file.close()
        return fileDict


def main():
    schemaFile, outputFile, wantDeprecated = loadOptions()

    schema = loadJson(schemaFile)
    if not schema:
        sys.exit(1)

    extension: str = outputFile.split('.')[-1].lower()
    generator = GeneratorManager.getGenerator(extension, wantDeprecated)
    if not generator:
        sys.exit(2)

    generator.beginFile()

    events = schema.pop("events", None)
    if events:
        for event in events:
            generator.documentEvent(event, events[event])

    hooks = schema.pop("hooks", None)
    if hooks:
        for hook in hooks:
            generator.documentHook(hook, hooks[hook])

    if not generator.toFile(outputFile):
        sys.exit(3)


if __name__ == "__main__":
    main()
