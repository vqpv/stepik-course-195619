def summa(n):
    if n == 1:
        return 1
    else:
        return n + summa(n - 1)
