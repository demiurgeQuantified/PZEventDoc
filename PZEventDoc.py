# if my work helped you, please consider leaving me a tip ^u^
# https://ko-fi.com/starseamstress

import json
from PZEDGlobals import *
import GeneratorManager
import pathlib
from generators import *


def document_from_json(
        input: str, format: str = "lua",
        want_deprecated: bool = False, want_events: bool = True,
        want_hooks: bool = True, want_callbacks: bool = True,
        deprecated_only: bool = False) -> str:
    """
    Documents the data stored in a JSON file as a string in the format specified.
    :param input: The full JSON text to read data from.
    :param format: The desired format for the output documentation. Valid options are "lua" and "md".
    :param want_deprecated: Whether to document deprecated objects from the data.
    :param want_events: Whether to document events from the data.
    :param want_hooks: Whether to document hooks from the data.
    :param want_callbacks: Whether to document callbacks from the data.
    :param deprecated_only: Whether to document only deprecated objects. Takes priority over want_deprecated.
    :return: The data documented in the format specified.
    """
    data = json.loads(input)

    deprecation_policy: WantDeprecated
    if deprecated_only:
        deprecation_policy = WantDeprecated.EXCLUSIVE
    else:
        deprecation_policy = WantDeprecated.ALLOW if want_deprecated else WantDeprecated.NONE

    generator = GeneratorManager.getGenerator(format, deprecation_policy)

    if want_events:
        events: dict = data.get("events")
        if events:
            for name, event in events.items():
                generator.documentEvent(name, event)

    if want_hooks:
        hooks: dict = data.get("hooks")
        if hooks:
            for name, hook in hooks.items():
                generator.documentHook(name, hook)

    if want_callbacks:
        callbacks: dict = data.get("callbacks")
        if callbacks:
            for name, callback in callbacks.items():
                generator.documentCallback(name, callback)

    return generator.get_final_string()


if __name__ == "__main__":
    import argparse

    arg_parser = argparse.ArgumentParser(epilog="If none of --events, --hooks, and --callbacks are set,"
                                                "all are treated as enabled.")

    arg_parser.add_argument("--input", "-i", default=None,
                            help="The path of the JSON file containing the data.")
    arg_parser.add_argument("--output", "-o", default="events.lua",
                            help="The filepath to write the documented data to.")
    arg_parser.add_argument("--events", action="store_true",
                            help="Enables documenting events.")
    arg_parser.add_argument("--hooks", action="store_true",
                            help="Enables documenting hooks.")
    arg_parser.add_argument("--callbacks", action="store_true",
                            help="Enables documenting callbacks.")
    arg_parser.add_argument("--generate_deprecated", default="false", nargs="?", const="true",
                            choices=["false", "true", "only"],
                            help="Whether to document deprecated objects.")
    arg_parser.add_argument("--format",
                            choices=["lua", "md"], default=None,
                            help="Which format to document in.")

    # temporary deprecated arguments
    arg_parser.add_argument("-d", action="store_true", default=None,
                            help="Deprecated. Use '--generate_deprecated enable' instead.")
    arg_parser.add_argument("-D", action="store_true", default=None,
                            help="Deprecated. Use '--generate_deprecated only' instead.")
    arg_parser.add_argument("-s", default=None,
                            help="Deprecated. Use --input instead.")

    args = arg_parser.parse_args()

    want_events = args.events
    want_hooks = args.hooks
    want_callbacks = args.callbacks
    # default behaviour: if no table flags are set, all types are enabled
    if not args.events and not args.hooks and not args.callbacks:
        want_events = True
        want_hooks = True
        want_callbacks = True

    want_deprecated = False
    deprecated_only = False
    if args.d is not None:
        want_deprecated = args.d
        print("DEPRECATION WARNING: Command line argument -d is deprecated. Use --help for information.")
    if args.D is not None:
        deprecated_only = args.D
        print("DEPRECATION WARNING: Command line argument -D is deprecated. Use --help for information.")

    output = args.output

    if args.generate_deprecated != "false":
        if args.generate_deprecated == "true":
            want_deprecated = True
        elif args.generate_depracted == "only":
            deprecated_only = True

    input_path: str | pathlib.PurePath
    if args.input is not None:
        input_path = args.input
    elif args.s is not None:
        print("DEPRECATION WARNING: Command line argument -s is deprecated. Use --help for information.")
        input_path = args.s
    else:
        input_path = pathlib.Path(__file__).parent / "data.json"

    file = open(input_path, 'r')
    input = file.read()
    file.close()

    format: str = args.format
    if format is None:
        format = args.output.split('.')[-1]

    file = open(output, 'w')
    file.write(
        document_from_json(
            input, format,
            want_deprecated, want_events, want_hooks, want_callbacks, deprecated_only))
    file.close()
