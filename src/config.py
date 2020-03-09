import json

def load_config():
    with open("splunk.json", "r") as f:
        return json.load(f)