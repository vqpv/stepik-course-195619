def flatten(lst):
    for l in lst:
        if isinstance(l, list):
            yield from flatten(l)
        else:
            yield l
