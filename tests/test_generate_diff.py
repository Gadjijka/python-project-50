import pytest
from gendiff.generate_diff import generate_diff
from gendiff.formats.format import choice_format


def read_file(file_name):
    with open(file_name) as file:
        return file.read()


@pytest.mark.parametrize('file1_name, file2_name, format', [
    ('file1.json', 'file2.json', 'stylish'),
    ('file1.yml', 'file2.yml', 'stylish'),
    ('file1.json', 'file2.json', 'plain'),
    ('file1.yml', 'file2.yml', 'plain'),
    ('file1.json', 'file2.json', 'json'),
    ('file1.yml', 'file2.yml', 'json')
])
def test_base_logic(file1_name, file2_name, format):
    file1_path = 'tests/fixtures/' + file1_name
    file2_path = 'tests/fixtures/' + file2_name
    assert (choice_format(generate_diff(file1_path, file2_path),
           format)) == read_file(f'tests/fixtures/expected_{format}.txt')[:-1]


def test_unsupported_formats():
    with pytest.raises(ValueError):
        choice_format(generate_diff('tests/fixtures/file1.json',
                      'tests/fixtures/file2.json'), 'png')
