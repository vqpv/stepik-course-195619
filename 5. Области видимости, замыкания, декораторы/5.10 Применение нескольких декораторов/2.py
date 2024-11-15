def double_it(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return inner
