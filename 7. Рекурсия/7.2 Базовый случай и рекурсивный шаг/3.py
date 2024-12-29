def sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_recursive(lst[1:])
