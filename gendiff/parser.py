import os
import yaml
import json


def load_file_from_path(path):
    format = get_file_format(path)
    content = get_file_content(path)
    return parse_data(content, format)


def parse_data(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ['yml', 'yaml']:
        return yaml.safe_load()
    raise FormatError(f'Unsupported file format: {format}')


def get_file_format(path):
    return os.path.splitext(path)[1][1:]


def get_file_content(path):
    with open(path) as file:
        return file.read()
