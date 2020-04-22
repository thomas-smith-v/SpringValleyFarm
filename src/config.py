import json
import os

def load_config():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/splunk.json", "r") as f:
        return json.load(f)