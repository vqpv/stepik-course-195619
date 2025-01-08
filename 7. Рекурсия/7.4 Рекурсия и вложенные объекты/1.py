def sum_recursive(lst):
    result = 0
    for v in lst:
        if isinstance(v, list):
            summa = sum_recursive(v)
            result += summa
        else:
            result += v
    return result
