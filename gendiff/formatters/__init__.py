from gendiff.formatters.json import form_to_json
from gendiff.formatters.plain import form_to_plain
from gendiff.formatters.stylish import form_to_stylish


FORMATS = {
    'json': form_to_json,
    'stylish': form_to_stylish,
    'plain': form_to_plain
}


def choice_format(data, format):
    if FORMATS.get(format) is not None:
        return FORMATS[format](data)
    raise ValueError(f'Unsupported format: {format}')
