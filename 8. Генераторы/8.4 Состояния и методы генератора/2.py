def alphabet():
    letter = yield
    while True:
        try:
            letter = yield DICTIONARY.get(letter, "default")
        except KeyError:
            letter = DICTIONARY.get(letter, "default")
