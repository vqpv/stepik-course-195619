def multiply(num):
    def inner(x):
        return x * num
    return inner
