from rosetta.lua.callback import LuaCallback
from rosetta.lua.parameter import LuaParameter
from rosetta.lua.return_value import LuaReturn


def parse_parameter(json: dict) -> LuaParameter:
    parameter = LuaParameter(json["name"])
    parameter.notes = json.get("notes", "")

    parameter.type = json["type"]
    parameter.optional = json.get("optional", False)
    parameter.nullable = json.get("nullable", False)

    return parameter


def parse_return(json: dict) -> LuaReturn:
    retval = LuaReturn(json.get("name", ""))
    retval.notes = json.get("notes", "")

    retval.type = json["type"]
    retval.nullable = json.get("nullable", False)

    return retval


def parse_callback(json: dict) -> LuaCallback:
    callback = LuaCallback(json.get("name", ""))
    callback.notes = json.get("notes", "")
    callback.tags = json.get("tags", callback.tags)

    for parameter in json["parameters"]:
        callback.parameters.append(parse_parameter(parameter))
    if (returns := json.get("return")) is not None:
        for retval in returns:
            callback.returns.append(parse_return(retval))

    return callback
