def validate_all_args_str(func):
    def inner(*args, **kwargs):
        if all([isinstance(i, str) for i in args]):
            return func(*args, **kwargs)
        else:
            print("Все аргументы должны быть строками")
            return None
    return inner


def validate_all_kwargs_int_pos(func):
    def inner(*args, **kwargs):
        if all([(type(i) is int and i > 0) for i in kwargs.values()]):
            return func(*args, **kwargs)
        else:
            print("Все именованные аргументы должны быть положительными числами")
            return None
    return inner
