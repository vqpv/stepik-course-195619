def check_count_args(func):
    def inner(*args, **kwargs):
        l = len(args) + len(kwargs)
        if l == 2:
            return func(*args, **kwargs)
        elif l < 2:
            print("Not enough arguments")
            return None
        elif l > 2:
            print("Too many arguments")
            return None
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
