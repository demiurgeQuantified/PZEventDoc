# if my work helped you, please consider leaving me a tip ^u^
# https://ko-fi.com/starseamstress

import sys
import json
from getopt import getopt
from PZEDGlobals import *
from generators.EmmyLuaGenerator import EmmyLuaGenerator


schemaFile: str = "schema.json"
outputFile: str = "Events.lua"
wantDeprecated: WantDeprecated = WantDeprecated.NONE


def loadOptions():
    global wantDeprecated, schemaFile, outputFile
    opts, _ = getopt(sys.argv[1:], "dDs:o:")
    for option, argument in opts:
        if option == "-d":
            wantDeprecated = WantDeprecated.ALLOW
        elif option == "-D":
            wantDeprecated = WantDeprecated.EXCLUSIVE
        elif option == "-i":
            schemaFile = argument
        elif option == "-o":
            outputFile = argument


def loadJson(filename: str) -> dict | None:
    try:
        file = open(filename, "r", encoding="utf-8")
    except OSError:
        print("ERROR: Failed to open " + schemaFile)
        return

    try:
        fileDict = json.loads(file.read())
    except json.JSONDecodeError:
        print("ERROR: " + schemaFile + " is not a valid JSON file.")
        return

    file.close()
    return fileDict


loadOptions()

generator = EmmyLuaGenerator(wantDeprecated)
schema = loadJson(schemaFile)
if not schema:
    sys.exit(1)

events = schema.pop("Events", [])
if events:
    for event in events:
        generator.documentEvent(event, events[event])

hooks = schema.pop("Hook", None) or schema.pop("Hooks", [])
if hooks:
    for hook in hooks:
        generator.documentHook(hook, hooks[hook])

if not generator.toFile(outputFile):
    sys.exit(1)
