def add_args(func):
    def inner(*args, **kwargs):
        args = list(args)
        args.insert(0, "begin")
        args.insert(len(args), "end")
        return func(*args, **kwargs)
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
