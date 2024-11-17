def validate_all_args_str(func):
    def inner(*args, **kwargs):
        if all([isinstance(i, str) for i in args]):
            return func(*args, **kwargs)
        else:
            print("Все аргументы должны быть строками")
            return None
    return inner
