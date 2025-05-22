class EventInvocation:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.arguments: list[str] = []


class Event:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.arguments: list[list[str]] = []


def merge_results(a: list[Event], b: list[Event]) -> list[Event]:
    event_dict = {event.name: event for event in a}
    for event in b:
        if event_dict.get(event.name) is None:
            event_dict[event.name] = event
        else:
            event_dict[event.name].arguments += event.arguments

    return list(event_dict.values())
