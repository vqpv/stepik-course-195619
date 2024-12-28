def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    min_n = int(lst[0])
    if min_n > find_min(lst[1:]):
        min_n = find_min(lst[1:])
    return min_n
