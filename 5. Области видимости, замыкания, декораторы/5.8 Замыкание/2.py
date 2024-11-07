def make_repeater(count):
    def inner(word):
        return word * count
    return inner
