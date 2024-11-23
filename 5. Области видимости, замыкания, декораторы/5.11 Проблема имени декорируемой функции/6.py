def reverse(func):
    def inner(*args, **kwargs):
        args = args[::-1]
        return func(*args)
    inner.__name__ = func.__name__
    return inner
