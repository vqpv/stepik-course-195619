def count_strings(*args):
    return sum(isinstance(arg, str) for arg in args)
