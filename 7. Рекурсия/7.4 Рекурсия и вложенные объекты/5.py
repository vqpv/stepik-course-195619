def is_member(n, lst):
    for i in lst:
        if isinstance(i, list) and is_member(n, i):
            return True
        elif n == i:
            return True
    return False
