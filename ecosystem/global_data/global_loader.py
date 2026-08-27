import json
import os

def load_global_data():
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "global.json")

    if not os.path.exists(config_path):
        return {}

    with open(config_path, "r") as f:
        data = json.load(f)

    return data
