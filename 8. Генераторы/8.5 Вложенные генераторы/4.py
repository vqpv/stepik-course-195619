def get_nested_dict_values(d):
    for _, v in d.items():
        if isinstance(v, dict):
            yield from get_nested_dict_values(v)
        else:
            yield v
