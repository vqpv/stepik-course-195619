def create_dict():
    k = 0
    d = {}
    def inner(v):
        nonlocal k
        k += 1
        d[k] = d.get(k, v)
        return d
    return inner
