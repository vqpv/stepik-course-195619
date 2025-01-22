def my_range_gen(n, i=0):
    if i != 0:
        i, n = n, i
    while i < n:
        yield i
        i += 1
