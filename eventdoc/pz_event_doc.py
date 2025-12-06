import pathlib
import zipfile
from warnings import deprecated

from eventdoc.analysis.rosetta_merge import RosettaMerger, PrintErrorHandler
from eventdoc.rendering import renderer_manager
from rosetta.game.projectzomboid.event import ZomboidEvent
from rosetta.game.projectzomboid.zomboid_root import ZomboidRoot
from rosetta.root import RosettaRoot
from rosetta import parser as rosetta_parser

from eventdoc.analysis.java_analyser import analyse_java
from eventdoc.analysis.lua_analyser import analyse_lua
from eventdoc.analysis.result import Event, merge_results


def render_from_analysis(game_path: pathlib.Path, desired_format: str,
                         rosetta: RosettaRoot | None = None,
                         want_deprecated: bool = False, want_events: bool = True,
                         want_hooks: bool = True, want_non_deprecated: bool = True) -> str:
    renderer = renderer_manager.get_renderer(desired_format)
    if renderer is None:
        return ""
    renderer.render_deprecated = want_deprecated
    renderer.render_non_deprecated = want_non_deprecated
    renderer.rosetta = rosetta

    events: list[Event] = []

    jar_file = game_path / "projectzomboid.jar"

    if jar_file.is_file():
        jar = zipfile.ZipFile(jar_file)
        for filename in jar.namelist():
            if not filename.endswith(".class") or not filename.startswith("zombie/"):
                continue
            if filename == "zombie/Lua/LuaEventManager.class":
                #  internal calls confuse the analyser and aren't needed anyway
                continue
            events = merge_results(events, analyse_java(zipfile.Path(jar, filename)))
    else:
        zombie_path = game_path / "zombie"

        for path, _, filenames in zombie_path.walk():
            for filename in filenames:
                if not filename.endswith(".class"):
                    continue
                if filename == "LuaEventManager.class":
                    #  internal calls confuse the analyser and aren't needed anyway
                    continue
                events = merge_results(events, analyse_java(path / filename))

    lua_path = game_path / "media" / "lua"

    for directory in [lua_path / "shared", lua_path / "client", lua_path / "server"]:
        for path, _, filenames in directory.walk():
            for filename in filenames:
                if not filename.endswith(".lua"):
                    continue
                events = merge_results(events, analyse_lua(path / filename))

    documentation: dict[str, ZomboidEvent] = {}
    if rosetta is not None:
        zomboid_root = rosetta.games.get("projectzomboid")
        if zomboid_root is not None:
            documentation = {
                event.name: event for event in zomboid_root.events
            }

    merger = RosettaMerger(rosetta)
    merger.error_handler = PrintErrorHandler()

    if want_events:
        seen_events: set[str] = set()
        for event in sorted(events, key=lambda e: e.name):
            doc = documentation.get(event.name)
            if doc is None:
                print(f"{event.name} has no documentation.")
            elif doc.deprecated:
                print(f"Event {event.name} is marked as deprecated, but has triggers.")
            renderer.add_event(
                merger.convert_event(event, doc)
            )
            seen_events.add(event.name)
        for event in documentation.values():
            if not event.deprecated and event.name not in seen_events:
                print(f"Documented event {event.name} is never triggered. Deprecation likely.")

    if want_hooks:
        # TODO: not implemented
        ...

    return renderer.render()


def render_from_rosetta(
        rosetta: RosettaRoot, desired_format: str,
        want_deprecated: bool = False, want_events: bool = True,
        want_hooks: bool = True, want_callbacks: bool = True,
        want_non_deprecated: bool = True) -> str:
    """
    Renders the data stored in a JSON file as a string in the format specified.
    :param rosetta: The Rosetta data to render objects from.
    :param desired_format: The desired format for the output documentation. Valid options are "lua" and "md".
    :param want_deprecated: Whether to render deprecated objects from the data.
    :param want_events: Whether to render events from the data.
    :param want_hooks: Whether to render hooks from the data.
    :param want_callbacks: Whether to render callbacks from the data.
    :param want_non_deprecated: Whether to render non-documented objects.
    :return: The data rendered in the format specified.
    """
    renderer = renderer_manager.get_renderer(desired_format)
    if renderer is None:
        return ""
    renderer.render_deprecated = want_deprecated
    renderer.render_non_deprecated = want_non_deprecated
    renderer.rosetta = rosetta

    assert rosetta.games.get("projectzomboid") is not None

    zomboid: ZomboidRoot = rosetta.games["projectzomboid"]

    if want_events:
        for event in sorted(zomboid.events, key=lambda e: e.name):
            renderer.add_event(event)

    if want_hooks:
        for hook in sorted(zomboid.hooks, key=lambda e: e.name):
            renderer.add_hook(hook)

    if want_callbacks:
        for name, callback in sorted(zomboid.callbacks.items()):
            renderer.add_callback(name, callback)

    return renderer.render()


@deprecated("Use render_from_rosetta instead.")
def document_from_json(
        json: str, desired_format: str,
        want_deprecated: bool = False, want_events: bool = True,
        want_hooks: bool = True, want_callbacks: bool = True,
        want_non_deprecated: bool = True) -> str:
    root = RosettaRoot()
    rosetta_parser.parse_json(root, json)

    if desired_format == "lua":
        desired_format = "luacats"

    return render_from_rosetta(
        root, desired_format,
        want_deprecated, want_events, want_hooks, want_callbacks, want_non_deprecated)
