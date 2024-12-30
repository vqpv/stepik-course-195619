def double_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return n * double_fact(n - 2)
