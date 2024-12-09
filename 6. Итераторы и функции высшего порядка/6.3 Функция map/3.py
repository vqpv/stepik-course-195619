def get_letters(s):
    return list(map(lambda x: (x.upper(), x.lower()), list(s)))
