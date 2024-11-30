def monkey_patching(arg="Monkey", kwarg="patching"):
    def decorator(func):
        def inner(*args, **kwargs):
            args = (arg,) * len(args)
            kwargs = {k: kwarg for k, v in kwargs.items()}
            return func(*args, **kwargs)
        inner.__name__ = func.__name__
        inner.__doc__ = func.__doc__
        return inner
    return decorator
