def limit_query(func):
    c = 3
    def inner(*args, **kwargs):
        nonlocal c
        if c > 0:
            c -= 1
            return func(*args, **kwargs)
        else:
            print("Лимит вызовов закончен, все 3 попытки израсходованы")
            return None
    inner.__name__ = func.__name__
    return inner
