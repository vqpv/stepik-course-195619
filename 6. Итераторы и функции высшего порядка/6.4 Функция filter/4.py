def filter_tuples(t: tuple) -> tuple:
    return tuple(filter(lambda x: (x[0] * x[1] * x[2]) == 60, t))
