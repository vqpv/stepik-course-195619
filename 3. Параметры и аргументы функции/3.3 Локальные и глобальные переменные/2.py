vowels = ['a','e', 'i', 'o', 'u']


def translate_to_robber_lang(s):
    result = ""
    for i in s:
        if i.isalpha() and i.lower() not in vowels:
            result += i + "o" + i
        else:
            result += i
    return result
