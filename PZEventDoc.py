import json

# PZEventDoc was written by Albion

schemaFile = "schema.json"
outputFile = "EventDoc.lua"
currentIndentation = 0

totalString = "-- Generated by PZEventDoc https://github.com/demiurgeQuantified/PZEventDoc\n\n-- If it helped you, please consider leaving me a tip ^u^\n-- https://ko-fi.com/starseamstress\n"
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



def getFunctionSignature(params):
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

def documentFunction(name, params=None):
    global totalString
    totalString += newLine() + ("---@param func {}" + newLine() + "{}").format(getFunctionSignature(params), writeFunction(name, ["func"]))



def getTableDescription(description="", deprecated=False, clientOnly=False, serverOnly=False):
    if clientOnly:
        description = "(Client Only) " + description
    elif serverOnly:
        description = "(Server Only) " + description
    if deprecated:
        description = "(Deprecated) " + description
    
    return description

def initTable(type):
    global totalString
    totalString += newLine() + type + " = {}\n"

def openTable(name, description=None):
    global totalString, currentIndentation
    if description != "":
        totalString += newLine() + "---" + description

    totalString += newLine() + name + " = {"
    currentIndentation += 1

def closeTable():
    global totalString, currentIndentation
    currentIndentation -= 1
    totalString += newLine() + "}"

def writeTable(event, data, tableName):     
    openTable(tableName + "." + event, getTableDescription(data.get("description", ""), data.get("deprecated", False), data.get("clientOnly", False), data.get("serverOnly", False)))

    documentFunction("Add", data.get("parameters"))
    documentFunction("Remove")

    closeTable()



def documentHook():
    openTable()

loadSchema()

events = schema.get("Events")
if events:
    initTable("Events")
    for event in events:
        writeTable(event, events[event], "Events")
    totalString += newLine()

hooks = schema.get("Hook") or schema.get("Hooks")
if hooks:
    initTable("Hook")
    for hook in hooks:
        writeTable(hook, hooks[hook], "Hook")
    totalString += newLine()

toFile(totalString)