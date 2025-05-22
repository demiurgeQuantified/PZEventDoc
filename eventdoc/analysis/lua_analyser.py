import pathlib
import contextlib
import os

from luaparser import ast
from luaparser.astnodes import Call, Name, String

from eventdoc.analysis.result import Event, EventInvocation


class EventCollector(ast.ASTVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.events: list[EventInvocation] = []

    def visit_Call(self, node: Call) -> None:
        if isinstance(node.func, Name) and node.func.id == "triggerEvent":
            event_name = node.args[0]
            assert isinstance(event_name, String)
            event = EventInvocation(event_name.s)
            # TODO: type is difficult to determine
            event.arguments = ["any" for _ in node.args[1:]]
            self.events.append(event)


def analyse_lua(path: pathlib.Path) -> list[Event]:
    with path.open('r') as file:
        source = file.read()

    # this function has a fancy print in it which is horrible for performance...
    # they removed the print but never released the update on pypi U_U
    with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
        tree = ast.parse(source)
        # FIXME: this bugs out when it reads \%
        #  is \% even valid in lua? onecompiler can't compile it for the same reason

    collector = EventCollector()
    collector.visit(tree)

    events: dict[str, Event] = {}
    for invocation in collector.events:
        event = events.get(invocation.name)
        if event is None:
            event = Event(invocation.name)
            events[invocation.name] = event
        event.arguments.append(invocation.arguments)

    # TODO: parameter names could be borrowed from event listeners

    return list(events.values())
