import pathlib

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.Token import Token
from antlr4.error.ErrorListener import ConsoleErrorListener

from luaparser import ast
from luaparser.ast import SyntaxException
from luaparser.astnodes import Call, Name, String, Chunk
from luaparser.builder import BuilderVisitor
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaParser import LuaParser

from eventdoc.analysis.result import Event, EventInvocation


# copy paste of ast.parse
# all this does is remove the print, because the __str__ is insanely expensive
# they fixed this months ago, but haven't actually updated the package
def parse(source: str) -> Chunk:
    """Parse Lua source to a Chunk."""
    lexer = LuaLexer(InputStream(source))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ConsoleErrorListener())

    token_stream = CommonTokenStream(lexer, channel=Token.DEFAULT_CHANNEL)
    parser = LuaParser(token_stream)
    parser.addErrorListener(ConsoleErrorListener())
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxException("syntax errors")
    else:
        v = BuilderVisitor(token_stream)
        val = v.visit(tree)
        return val


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

    try:
        tree = parse(source.replace("\\%", "%"))
        # this bugs out when it reads \%
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

        # TODO: parameter names could be borrowed from callbacks

        return list(events.values())
    except SyntaxException as e:
        print(f"Error parsing {path!s}: {e!s}")
        return []
