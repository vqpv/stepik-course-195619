def alphabet():
    letter = yield
    while True:
        letter = yield DICTIONARY[letter]
