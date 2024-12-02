def compose(*funcs):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            for f in funcs:
                result = f(result)
            return result
        return inner
    return decorator
