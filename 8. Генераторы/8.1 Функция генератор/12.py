def my_range_gen(n, i=None, s=1):
    if s != 0:
        if i == None:
            i = 0
            while i < n:
                yield i
                i += s
        elif i and i != 0:
            i, n = n, i
            if n > i and s > 0:
                while i < n:
                    yield i
                    i += s
            elif n < i and s < 0:
                while i > n:
                    yield i
                    i += s
        elif i == 0 and s < 0:
            while n > i:
                yield n
                n += s
