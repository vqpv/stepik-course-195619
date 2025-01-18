def gen_fibonacci_numbers(n):
    x, y = 1, 1
    for _ in range(n):
        yield x
        x, y = y, x + y
