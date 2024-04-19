def generator(first_file, second_file):
    difference = []
    keys = first_file.keys() | second_file.keys()
    for key in keys:
        first_value = first_file.get(key)
        second_value = second_file.get(key)
        if key in second_file.keys() and key not in first_file.keys():
            difference.append(to_add(key, second_value))
        elif key in first_file.keys and key not in second_file.keys():
            difference.append(to_delete(key, first_value))
        elif isinstance(first_value, dict) and isinstance(second_value, dict):
            difference.append(nested(key, first_value, second_value))
        elif first_value != second_value:
            difference.append(modified(key, first_value, second_value))
        else:
            difference.append(unchanged(key, first_value))
    return sorted(difference, key=lambda x: x['name'])


def nested(key, first_value, second_value):
    return {
        'action': 'nested',
        'name': key,
        'children': generator(first_value, second_value)
    }


def to_add(key, second_value):
    return {
        'action': 'added',
        'name': key,
        'new_value': second_value
    }


def to_delete(key, first_value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': first_value
    }


def modified(key, first_value, second_value):
    return {
        'action': 'modified',
        'name': key,
        'new_value': second_value,
        'old_value': first_value
    }


def unchanged(key, first_value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': first_value
    }
