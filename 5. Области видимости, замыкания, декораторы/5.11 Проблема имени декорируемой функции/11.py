def counting_calls(func):
    call_count = 0
    calls = []
    def inner(*args, **kwargs):
        nonlocal call_count, calls
        call_count += 1
        calls.append({'args': args, 'kwargs': kwargs})
        inner.call_count = call_count
        return func(*args, **kwargs)
    inner.call_count = call_count
    inner.calls = calls
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
