def convert_to(t):
    def decorator(func):
        def inner(*args, **kwargs):
            return t(func(*args, **kwargs))
        inner.__name__ = func.__name__
        inner.__doc__ = func.__doc__
        return inner
    return decorator
