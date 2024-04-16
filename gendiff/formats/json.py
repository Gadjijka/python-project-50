import json


def form_to_json(data):
    return json.dumps(data, indent=4, separators=(',', ': '))
