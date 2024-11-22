def explicit_args(func):
    def inner(*args, **kwargs):
        if args:
            print("Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений")
            return None
        else:
            return func(*args, **kwargs)
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
