def limit_query(limit):
    def decorator(func):
        c = limit
        def inner(*args, **kwargs):
            nonlocal c
            if c > 0:
                c -= 1
                return func(*args, **kwargs)
            else:
                print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")
                return None
        inner.__name__ = func.__name__
        return inner
    return decorator
