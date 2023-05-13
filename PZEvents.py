import json

schemaFile = "schema.json"
outputFile = "EventDoc.lua"
currentIndentation = 0

totalString = ""
schema = {}

def loadSchema():
    global schema
    file = open(schemaFile, "r", encoding="utf-8")
    schema = json.loads(file.read())
    file.close()

def toFile(str):
    file = open(outputFile, "w", encoding="utf-8")
    file.write(str)
    file.close()



def newLine():
    return "\n" + "    " * currentIndentation

def getFunctionDescriptor(params):
    if not isinstance(params, dict) or len(params) == 0:
        return "function"
    
    formattedParams = ""
    doComma = False
    for label in params:
        if doComma:
            formattedParams += ","
        else:
            doComma = True

        formattedParams += label + ":" + params[label]

    return "fun({}):any".format(formattedParams)


def createEventsTable():
    global totalString
    totalString += "Events = {}\n"

def openEvent(event, description=None):
    global totalString, currentIndentation
    if description:
        totalString += newLine() + "---" + description

    totalString += newLine() + "Events." + event + " = {"
    currentIndentation += 1

def closeEvent():
    global totalString, currentIndentation
    currentIndentation -= 1
    totalString += newLine() + "}"

def writeFunction(name, args=None):
    formattedArgs = ""
    if not (args == None or len(args) == 0):
        doComma = False
        for label in args:
            if doComma:
                formattedArgs += ", "
            else:
                doComma = True
            formattedArgs += label

    return "{} = function({}) end,".format(name, formattedArgs)

def documentEventFunction(name, params=None):
    global totalString
    totalString += newLine() + ("---@param func {}" + newLine() + "{}").format(getFunctionDescriptor(params), writeFunction(name, ["func"]))

def documentEvent(event, data):
    openEvent(event, data.get("description"))
    documentEventFunction("Add", data.get("parameters"))
    documentEventFunction("Remove")
    closeEvent()

loadSchema()
createEventsTable()

for event in schema:
    documentEvent(event, schema[event])

toFile(totalString)