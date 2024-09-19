def is_only_one_positive(*args):
    return len(list(filter(lambda x: x > 0, args))) == 1
