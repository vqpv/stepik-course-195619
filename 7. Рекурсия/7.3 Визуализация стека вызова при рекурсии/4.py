def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word.lower()[0] != word.lower()[-1]:
        return False
    return is_palindrome(word[1:-1])
