import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'config/request_bodies.json')


def load_json_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
