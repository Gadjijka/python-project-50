from gendiff.base_logic import base_logic
from gendiff.parser import load_file_from_path


def make_a_difference(first_path, second_path):
    first_file = load_file_from_path(first_path)
    second_file = load_file_from_path(second_path)
    return base_logic(first_file, second_file)
