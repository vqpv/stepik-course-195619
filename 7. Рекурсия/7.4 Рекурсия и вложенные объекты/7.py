def reversed_recursive(lst):
    if isinstance(lst, list):
        return [reversed_recursive(i) if isinstance(i, list) else i for i in reversed(lst)]
    else:
        return lst
