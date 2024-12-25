def print_from(n):
    if n > 0:
        print(n)
        n -= 1
        return print_from(n)
