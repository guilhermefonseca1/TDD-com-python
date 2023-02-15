import json

class MissingFileException(Exception):
    pass

def load_json(path):
    if not path.lower().endswith('.json'):
        raise ValueError
    try:
        with open(path) as file:
            return json.load(file)
    except FileNotFoundError:
        raise MissingFileException