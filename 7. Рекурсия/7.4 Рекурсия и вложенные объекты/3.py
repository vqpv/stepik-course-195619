def get_max_recursive(lst):
    result = float('-inf')
    for v in lst:
        if isinstance(v, list):
            maximum = get_max_recursive(v)
            if maximum > result:
                result = maximum
        else:
            if v > result:
                result = v
    return result
