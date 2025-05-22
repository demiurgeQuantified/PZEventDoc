# PZEventDoc
PZEventDoc is a tool for generating documentation for Project Zomboid events and hooks from JSON data to allow for type
checking and written documentation with unified information. It is primarily used to generate [Umbrella](https://github.com/asledgehammer/Umbrella), but can be used to document custom events too.

## Requirements
PZEventDoc requires Python 3.11 or above.
In order to analyse code, it also requires the pip packages `luaparser` and `kirjava-jvm`.

## Usage
``python main.py "data.json" "events.lua"``

Launch with -h for details on command line arguments.

## Code Analysis
PZEventDoc has a work-in-progress capability to automatically detect registered events and their parameters by analysing Java bytecode and Lua source code. This functionality isn't quite good enough yet to be relied upon for data generation without human modification, however it can be very useful for detecting newly added/changed events and error checking the existing data. Pass the directory of your game installation with `--game_path` to run analysis. Rosetta data will be used for parameter names and descriptions when it matches the analysis. 
