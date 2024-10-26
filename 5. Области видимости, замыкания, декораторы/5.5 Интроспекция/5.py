def find_keys(**kwargs):
    return sorted([key for key, value in kwargs.items() if isinstance(value, list) or isinstance(value, tuple)], key=lambda x: x.lower())
