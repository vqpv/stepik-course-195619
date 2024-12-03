def add_attrs(**kw):
    def decorator(func):
        for attr_name, attr_value in kw.items():
            setattr(func, attr_name, attr_value)
        return func
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return decorator
