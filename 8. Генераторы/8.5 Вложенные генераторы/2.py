def merge_generators(*args):
    for arg in args:
        yield from arg
