def is_member(value, lst):
    if not lst:
        return False
    elif value == lst[0]:
        return True
    return is_member(value, lst[1:])
