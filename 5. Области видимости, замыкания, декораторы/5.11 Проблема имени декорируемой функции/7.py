def monkey_patching(func):
    def inner(*args, **kwargs):
        args = ("Monkey",) * len(args)
        kwargs = {k: "patching" for k, v in kwargs.items()}
        return func(*args, **kwargs)
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
