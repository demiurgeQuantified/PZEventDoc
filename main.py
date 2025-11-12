import argparse
import pathlib
import sys

from rosetta import parser as rosetta_parser
from eventdoc import pz_event_doc
from rosetta.root import RosettaRoot


def main():
    arg_parser = argparse.ArgumentParser(epilog="If none of --events, --hooks, and --callbacks are set,"
                                                "all are treated as enabled.")

    arg_parser.add_argument("input",
                            help="The path of the JSON file or directory of JSON files containing Rosetta data.",
                            type=pathlib.Path)
    arg_parser.add_argument("output",
                            help="The filepath to write the documented data to.",
                            type=pathlib.Path)
    arg_parser.add_argument("--events", action="store_true",
                            help="Enables documenting events.")
    arg_parser.add_argument("--hooks", action="store_true",
                            help="Enables documenting hooks.")
    arg_parser.add_argument("--callbacks", action="store_true",
                            help="Enables documenting callbacks.")
    arg_parser.add_argument("--render_deprecated", default="false", nargs="?", const="true",
                            choices=["false", "true", "only"],
                            help="Whether to document deprecated objects.")
    arg_parser.add_argument("--format",
                            choices=["lua", "md", "luacats", "emmylua"], default=None,
                            help="Which format to document in.")
    arg_parser.add_argument("--game_path", default=None,
                            help="Base path of a Project Zomboid installation (ProjectZomboid/). If specified, the game"
                                 " will be scanned for event triggers.")

    args = arg_parser.parse_args()

    want_events = args.events
    want_hooks = args.hooks
    want_callbacks = args.callbacks
    # default behaviour: if no table flags are set, all types are enabled
    if not args.events and not args.hooks and not args.callbacks:
        want_events = True
        want_hooks = True
        want_callbacks = True

    want_non_deprecated = True
    want_deprecated = False
    output_path: pathlib.Path = args.output

    if args.render_deprecated != "false":
        want_deprecated = True
        if args.render_deprecated == "only":
            want_non_deprecated = False

    input_path: pathlib.Path = args.input

    if not input_path.exists():
        print(f"Input path {input_path} does not exist.")
        sys.exit(1)

    root = RosettaRoot()
    if input_path.is_file():
        rosetta_parser.add(root, input_path)
    else:
        for directory, _, filenames in input_path.walk():
            for filename in filenames:
                rosetta_parser.add(root, directory / filename)

    desired_format: str = args.format
    if desired_format is None:
        desired_format = output_path.name.split('.')[-1]
        if desired_format == "lua":
            desired_format = "luacats"

    game_path: pathlib.Path | None = None
    if args.game_path is not None:
        game_path = pathlib.Path(args.game_path)

    if desired_format == "lua":
        print("--format lua is deprecated, use --format luacats or --format emmylua instead")
        desired_format = "luacats"

    if game_path is not None:
        rendered_text = pz_event_doc.render_from_analysis(
            game_path, desired_format,
            rosetta=root,
            want_events=want_events, want_hooks=want_hooks,
            want_deprecated=want_deprecated, want_non_deprecated=want_non_deprecated
        )
    else:
        rendered_text = pz_event_doc.render_from_rosetta(
            root, desired_format,
            want_events=want_events, want_hooks=want_hooks, want_callbacks=want_callbacks,
            want_deprecated=want_deprecated, want_non_deprecated=want_non_deprecated)

    if rendered_text == "":
        print("Rendering failed.")
        sys.exit(1)

    if desired_format == "luacats" or desired_format == "emmylua":
        # this path could be user defined
        extra_path = pathlib.Path(__file__).parent / "extra.lua"
        if extra_path.exists() and extra_path.is_file():
            with extra_path.open('r') as file:
                rendered_text = file.read() + "\n" + rendered_text

    with output_path.open('w') as file:
        file.write(rendered_text)


if __name__ == "__main__":
    main()
