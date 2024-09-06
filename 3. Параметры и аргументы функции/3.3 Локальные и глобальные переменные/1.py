alpha = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(s):
    result = True
    for i in alpha:
        if i in s.lower():
            continue
        else:
            result = False
            break
    return result
