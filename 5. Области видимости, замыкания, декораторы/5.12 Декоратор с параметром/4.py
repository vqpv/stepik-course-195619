def pass_arguments(*args, **kwargs):
    def decorator(func):
        def inner(*inner_args, **inner_kwargs):
            return func(*inner_args, *args, **inner_kwargs, **kwargs)
        inner.__name__ = func.__name__
        inner.__doc__ = func.__doc__
        return inner
    return decorator
