def repeater(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner
