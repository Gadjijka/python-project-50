from gendiff.formats.json import form_to_json
from gendiff.formats.plain import form_to_plain
from gendiff.formats.stylish import form_to_stylish


FORMATS {'json': form_to_json, 'stylish': form_to_stylish, 'plain': form_to_plain}


def choice_format(data, format):
    if FORMATS.get(format) != None:
        return FORMATS[format](data)
    raise FormatError(f'Unsupported format: {format}')

