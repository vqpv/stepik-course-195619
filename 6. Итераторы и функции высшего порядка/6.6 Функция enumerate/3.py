def get_words_with_position(words):
    return [(j, i + 1) for i, j in enumerate(words.split())]
