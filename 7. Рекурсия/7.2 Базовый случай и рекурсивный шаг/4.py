def sum_digits(n):
    return n if n % 10 == 0 else n % 10 + sum_digits(n // 10)
