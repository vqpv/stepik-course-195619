def gen_factorial():
    factorial = 1
    n = 1
    while True:
        factorial *= n
        yield factorial
        n += 1
