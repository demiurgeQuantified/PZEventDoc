import copy
import sys
import json


def update_callback(callback: dict):
    if (retval := callback.get("returns")) is not None:
        callback.pop("returns")
        callback["return"] = [retval]
    else:
        callback["return"] = []


def main():
    file = open(sys.argv[1], 'r')
    old_json = json.load(file)
    file.close()

    new_json = {
        "version": "1.1",
        "games": {
            "projectzomboid": {
                "events": [],
                "hooks": [],
                "callbacks": {}
            }
        }
    }
    events = new_json["games"]["projectzomboid"]["events"]
    hooks = new_json["games"]["projectzomboid"]["hooks"]
    callbacks = new_json["games"]["projectzomboid"]["callbacks"]

    for name, event in old_json["events"].items():
        new_event = {"name": name}
        # not using copy.deepcopy because i need to add the name first for formatting reasons
        for key, value in event.items():
            new_event[key] = copy.deepcopy(value)
        update_callback(event["callback"])
        events.append(new_event)

    for name, hook in old_json["hooks"].items():
        new_hook = {"name": name}
        for key, value in hook.items():
            new_hook[key] = copy.deepcopy(value)
        update_callback(hook["callback"])
        hooks.append(new_hook)

    for name, callback in old_json["callbacks"].items():
        callback = copy.deepcopy(callback)
        update_callback(callback)
        callbacks["umbrella." + name] = callback

    file = open(sys.argv[2], 'w')
    json.dump(new_json, file, indent=4)
    file.close()


if __name__ == "__main__":
    main()
