def multu_recursive(lst):
    result = 1
    for v in lst:
        if isinstance(v, list):
            p = multu_recursive(v)
            result *= p
        else:
            if isinstance(v, int):
                result *= v
    return result
