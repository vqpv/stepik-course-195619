def filter_even(func):
    def inner(*args, **kwargs):
        args = list(filter(lambda x: ((x is int and x % 2 == 0) or (type(x) in [str, tuple, list, dict] and len(x) % 2 == 0)), args))
        return func(*args, **kwargs)
    return inner


def delete_short(func):
    def inner(*args, **kwargs):
        kwargs = {i: j for i, j in kwargs.items() if len(i) > 4}
        return func(*args, **kwargs)
    return inner
