from gendiff.generator import generator
from gendiff.parser import load_file_from_path
from gendiff.formats.format import choice_format


def generate_diff(first_path, second_path, format):
    first_file = load_file_from_path(first_path)
    second_file = load_file_from_path(second_path)
    return choice_format(generator(first_file, second_file), format)
