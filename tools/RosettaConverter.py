import sys
import json


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


def writeJson(data: dict, path: str):
    """
    Writes a dictionary as a json file

    :param data: The dictionary to write
    :param path: The path of the file to write
    :return:
    """
    file = open(path, "w", encoding="utf-8")

    file.write(json.dumps(data, indent=4))
    file.close()


def convertEvent(event: dict) -> dict:
    """
    Takes an old format event definition and returns a Rosetta definition of the same event.

    Events having multiple callback signatures is not supported in the new format - the first entry will be used in the new definition.

    :param event: Old format event definition
    :return: Rosetta format event definition
    """
    newEvent: dict = {}

    newEvent["notes"] = event.get("description", "")

    contexts: dict | None = event.get("context")
    if contexts:
        newContexts: dict = {}
        for context in contexts:
            if contexts[context]:  # contexts default to true so we can just drop them
                continue
            newContexts[context] = False
        newEvent["context"] = newContexts

    parameters: dict | None = event.get("parameters")
    if parameters:
        callback: list[dict] = []
        if isinstance(parameters, list):  # supporting multiple signatures this way wasn't smart
            parameters = parameters[0]
        for paramName, paramType in parameters.items():
            callback.append({"name": paramName, "type": paramType})
        newEvent["callback"] = {"parameters": callback}

    deprecated = event.get("deprecated")
    if deprecated:  # defaults to false so we can just drop it
        newEvent["deprecated"] = True

    return newEvent


def convertHook(hook: dict) -> dict:
    """
    Takes an old format hook definition and returns a Rosetta definition of the same hook.

    :param hook: Old format event definition
    :return: Rosetta format event definition
    """
    return convertEvent(hook)
    # hooks currently use the same format as events in both schemas
    # as rosetta isn't finalised i'm keeping this function separate just in case


def oldToRosetta(data: dict) -> dict:
    """
    Converts an old format event/hook definition dictionary to the Rosetta format

    :param data: Old format event/hook definitions
    :return: Rosetta format event/hook definitions
    """
    newData: dict[str, dict] = {}

    oldEvents: dict[str, dict] | None = data.get("Events")
    if oldEvents:
        events: dict[str, dict] = {}
        for eventName in oldEvents:
            events[eventName] = convertEvent(oldEvents[eventName])
        newData["events"] = events

    oldHooks: dict[str, dict] | None = data.get("Hooks")
    if oldHooks:
        hooks: dict[str, dict] = {}
        for hookName in oldHooks:
            hooks[hookName] = convertHook(oldHooks[hookName])
        newData["hooks"] = hooks

    return newData


if __name__ == "__main__":
    try:
        try:
            inFile: str = sys.argv[1]
        except IndexError:
            raise Exception("No input file provided")

        try:
            filepath, extension = inFile.rsplit(".", 1)
        except ValueError:
            raise Exception("Input file path is invalid")
        if extension != "json":
            raise Exception("Input file is not a json file")

        rosettaData = oldToRosetta(readJson(inFile))
        writeJson(rosettaData, filepath + "-rosetta.json")
    except Exception as e:
        print("Conversion failed: " + str(e))
