# PZEventDoc
PZEventDoc is a tool for generating Lua annotations for Project Zomboid events and hooks from a JSON specification to allow for autocompletion, type checking and easy access to documentation. Most modders will only be interested in the [output files](../../../PZEventStubs/).

## Command Line Arguments
| Option | Arguments | Effect |
| --- | --- | --- |
| -d | None | Deprecated events will be included in the generated file |
| -D | None | The generated file will only contain deprecated events |
| -s | File path ending in ".json" | The JSON schema file to generate from |
| -o | File path ending in ".lua" | The Lua file to write to. Any existing file will be overwritten. |
