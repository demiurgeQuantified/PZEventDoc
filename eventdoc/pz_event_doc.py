import pathlib

from eventdoc.analysis.rosetta_merge import convert_event, PrintErrorHandler
from eventdoc.rendering import renderer_manager
from rosetta.game.projectzomboid.event import ZomboidEvent
from rosetta.game.projectzomboid.zomboid_root import ZomboidRoot
from rosetta.root import RosettaRoot
from rosetta import parser as rosetta_parser

from eventdoc.analysis.java_analyser import analyse_java
from eventdoc.analysis.result import Event, merge_results


def document_from_analysis(game_path: pathlib.Path, desired_format: str,
                           rosetta: str = "",
                           want_deprecated: bool = False, want_events: bool = True,
                           want_hooks: bool = True, want_non_deprecated: bool = True) -> str:
    renderer = renderer_manager.get_renderer(desired_format)
    if renderer is None:
        return ""
    renderer.render_deprecated = want_deprecated
    renderer.render_non_deprecated = want_non_deprecated

    zombie_path = game_path / "zombie"
    events: list[Event] = []

    # events = analyse_java(zombie_path / "network" / "fields" / "hit" / "WeaponHit.class")

    for path, _, filenames in zombie_path.walk():
        for filename in filenames:
            if not filename.endswith(".class"):
                continue
            if filename == "LuaEventManager.class":
                #  internal calls confuse the analyser and aren't needed anyway
                continue
            events = merge_results(events, analyse_java(path / filename))

    documentation: dict[str, ZomboidEvent] = {}
    if rosetta != "":
        root = RosettaRoot()
        rosetta_parser.parse_json(root, rosetta)
        zomboid_root = root.games["projectzomboid"]
        documentation = {
            event.name: event for event in zomboid_root.events
        }

    error_handler = PrintErrorHandler()

    if want_events:
        for event in events:
            if documentation.get(event.name) is None:
                print(event.name + " has no documentation.")
            renderer.add_event(
                convert_event(event, documentation.get(event.name), error_handler)
            )

    if want_hooks:
        # TODO: not implemented
        ...

    return renderer.render()


def document_from_json(
        input_string: str, desired_format: str,
        want_deprecated: bool = False, want_events: bool = True,
        want_hooks: bool = True, want_callbacks: bool = True,
        want_non_deprecated: bool = True) -> str:
    """
    Renders the data stored in a JSON file as a string in the format specified.
    :param input_string: The full JSON text to read data from.
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

    root = RosettaRoot()
    if not rosetta_parser.parse_json(root, input_string):
        return ""

    assert root.games.get("projectzomboid") is not None

    zomboid: ZomboidRoot = root.games["projectzomboid"]

    if want_events:
        for event in zomboid.events:
            renderer.add_event(event)

    if want_hooks:
        for hook in zomboid.hooks:
            renderer.add_hook(hook)

    if want_callbacks:
        for name, callback in zomboid.callbacks.items():
            renderer.add_callback(name, callback)

    return renderer.render()
