def is_palindrome():
    n = yield
    while True:
        n = yield str(n) == str(n)[::-1]
