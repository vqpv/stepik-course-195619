def counting_calls(func):
    call_count = 0
    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        inner.call_count = call_count
        return func(*args, **kwargs)
    inner.call_count = call_count
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
