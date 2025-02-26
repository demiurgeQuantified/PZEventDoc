from .context import ZomboidContext
from .event import ZomboidEvent
from .zomboid_callback import ZomboidCallback
from ...lua import lua_parser
from .zomboid_root import ZomboidRoot


def parse_context(context: ZomboidContext, json: dict):
    context.server = json.get("server", True)
    context.client = json.get("client", True)
    context.singleplayer = json.get("singleplayer", True)
    context.multiplayer = json.get("multiplayer", True)


def parse_callback(json: dict) -> ZomboidCallback:
    callback = ZomboidCallback(json.get("name", ""))
    callback.notes = json.get("notes", "")
    callback.tags = json.get("tags", callback.tags)

    for parameter in json["parameters"]:
        callback.parameters.append(lua_parser.parse_parameter(parameter))
    if (returns := json.get("return")) is not None:
        for retval in returns:
            callback.returns.append(lua_parser.parse_return(retval))

    if (context := json.get("context")) is not None:
        parse_context(callback.context, context)

    return callback


def parse_events(json: list[dict]) -> list[ZomboidEvent]:
    events = []
    for event_definition in json:
        event = ZomboidEvent(event_definition["name"])
        event.notes = event_definition.get("notes", "")
        if (tags := event_definition.get("tags")) is not None:
            event.tags += tags
        event.deprecated = event_definition.get("deprecated", False)

        event.callback = parse_callback(event_definition["callback"])

        if (context := event_definition.get("context")) is not None:
            parse_context(event.context, context)

        events.append(event)

    return events


def parse_zomboid(zomboid: ZomboidRoot, json: dict) -> bool:
    if (events := json.get("events")) is not None:
        zomboid.events += parse_events(events)

    if (hooks := json.get("hooks")) is not None:
        zomboid.hooks += parse_events(hooks)

    if (callbacks := json.get("callbacks")) is not None:
        for name, callback in callbacks.items():
            zomboid.callbacks[name] = parse_callback(callback)
    return True
