def form_to_plain(data):
    result = []
    for step in data:
        formatted_step = make_plain(step, path)
        if formatted_step is not None:
            result.append(formatted_step)
    return '\n'.join(result)


def make_plain(step, path = ''):
    current_key = step.get('name')
    current_path = f"{path}.{current_key}" if path else current_key
    action = step.get('action')
    new_value = to_str(step.get('new_value'))
    old_value = to_str(step.get('old_value'))
    if action == 'added':
        return f'Property "{current_path}" was added with value: {new_value}'
    if action == 'deleted':
        return f'Property "{current_path}" was removed'
    if action == 'modified':
        return (
	    f'Property "{current_path}" was updated.'
	    f'From {old_value} to {new_value}'
	)
    if action == 'nested':
        children = step.get('children')
        return make_plain(children, current_path)
    return None


def to_str(item):
    if isinstance(item, (list, dict)):
        return '[complex value]'
    elif item is None:
	return 'null'
    elif isinstance(value, bool):
	return str(item).lower()
    elif isinstance(item, str):
	return f"'{item}'"
    else:
	return str(item)
