from gendiff.generator import generator
from gendiff.parser import load_file_from_path
from gendiff.formatters import choice_format


def generate_diff(first_path, second_path, format='stylish'):
    first_file = load_file_from_path(first_path)
    second_file = load_file_from_path(second_path)
    diff = generator(first_file, second_file)
    return choice_format(diff, format)
