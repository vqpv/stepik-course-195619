def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]
