import os
import yaml
import json


def load_file_from_path(path):
    type_ = get_file_format(path)
    if type_ == 'json':
        return json.load(open(path))
    if type_ in ['yml', 'yaml']:
        return yaml.safe_load(open(path))
    raise ValueError(f'Unsupported file format: {format}')


def get_file_format(path):
    return os.path.splitext(path)[1][1:]
