# PZEventDoc
PZEventDoc is a tool for generating Lua annotations for Project Zomboid events and hooks from a JSON specification to allow for autocompletion, type checking and easy access to documentation. Most modders will only be interested in the [output files](https://github.com/demiurgeQuantified/PZEventStubs).

## Command Line Arguments
| Option   | Arguments         | Effect                                         |
|----------|-------------------|------------------------------------------------|
| --input  | File path         | The path of the JSON file containing the data. |
| --output | File path         | The filepath to write the documented data to.  |
| --events | None              | Enables documenting events.                    |
| --hooks | None              | Enables documenting hooks.                     |
| --callbacks | None              |  Enables documenting callbacks.                |
| --generate_deprecated | false\|true\|only | Whether to document deprecated objects.        |
| --format | lua\|md           | Which format to document in. |