def make_strings_big(*args, reverse=False):
    if reverse:
        [print(i.lower()) for i in args]
    else:
        [print(i.upper()) for i in args]
