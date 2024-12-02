def validate_all_args(t):
    def decorator(func):
        def inner(*args, **kwargs):
            if all([isinstance(i, t) for i in args]):
                return func(*args, **kwargs)
            else:
                print(f"Все аргументы должны принадлежать типу {t}")
                return None
        return inner
    return decorator
