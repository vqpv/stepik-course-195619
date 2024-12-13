def filter_words(w):
    return list(filter(lambda x: len(x) == 4 or x.startswith("S"), w))
