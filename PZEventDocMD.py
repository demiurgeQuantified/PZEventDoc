"""
MIT License

Copyright (c) 2023 Albion

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# if it work helped you, please consider leaving me a tip ^u^
# https://ko-fi.com/starseamstress

import json

schemaFile = "schema.json"
outputFile = "reference/Events.md"

def loadSchema():
    global schema
    file = open(schemaFile, "r", encoding="utf-8")
    schema = json.loads(file.read())
    file.close()

def toFile():
    file = open(outputFile, "w", encoding="utf-8")
    file.write(totalString)
    file.close()



def getParameterString(parameters):
    result = ""
    if isinstance(parameters, list):
        for i in range(len(parameters)):
            result += "{}: {}".format(i + 1, getParameterString(parameters[i]))
        return result
    
    for param in parameters:
        result += "{} {}, ".format(parameters[param], param)
    return result

def getTableDescription(description="", deprecated=False, context={}):
    if context.get("multiplayer", True):
        if context.get("client", True):
            if not context.get("server", True):
                description = "(Client) " + description
        else:
            description = "(Server) " + description

        if not context.get("singleplayer", True):
            description = "(Multiplayer) " + description
    else:
        description = "(Singleplayer) " + description

    if deprecated:
        description = "(Deprecated) " + description
    
    return description

totalString = ""

loadSchema()

events = schema.pop("Events", None)
if events:
    totalString += "# Events\nEvent | Description | Parameters\n--- | --- | ---\n"
    for event in events:
        data = events[event]
        totalString += "{} | {} | {}\n".format(event,
                                               getTableDescription(data.get("description", ""),
                                                                   data.get("deprecated", False),
                                                                   data.get("context", {})),
                                               getParameterString(data.get("parameters", {})))
        

hooks = schema.pop("Hook", None) or schema.pop("Hooks", None)
if hooks:
    totalString += "\n# Hooks\nHook | Description | Parameters\n--- | --- | ---\n"
    for hook in hooks:
        data = hooks[hook]
        totalString += "{} | {} | {}\n".format(hook,
                                        getTableDescription(data.get("description", ""),
                                                            data.get("deprecated", False),
                                                            data.get("context", {})),
                                        getParameterString(data.get("parameters", {})))


toFile()