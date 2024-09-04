def is_member(value, lst):
    return value in lst


def overlapping(lst_1, lst_2):
    return any([is_member(i, lst_2) for i in lst_1])
