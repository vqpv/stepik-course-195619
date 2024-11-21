def no_side_effects_decorator(func):
    def inner(*args, **kwargs):
        return func(args[0].copy(), *args[1:], **kwargs)
    inner.__name__ = func.__name__
    return inner
