# PZEventDoc
PZEventDoc is a tool for generating Lua documentation for Project Zomboid events and hooks to improve intellisense features.
## Usage
If you are a modder, download the generated Lua file(s) from the [Releases](../../releases/) page and add them as a library to your IDE. The Events-deprecated.lua file contains events that aren't actually used by the game anymore, included only for completeness. In most cases you will not want this file.


For those interested in generating their own documentation, you can copy the format from the provided schema.json. When running the script from the command line, you can pass several command line options:
| Option | Arguments | Effect |
| --- | --- | --- |
| -d | None | Deprecated events will be included in the generated file |
| -D | None | The generated file will only contain deprecated events |
| -s | File path ending in ".json" | The JSON schema file to generate from |
| -o | File path ending in ".lua" | The Lua file to write to. Any existing file will be overwritten. |
