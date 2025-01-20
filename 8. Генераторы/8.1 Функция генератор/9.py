def my_enumerate(lst, s=0):
    i = s
    while s < len(lst) + i:
        yield s, lst[s - i]
        s += 1
