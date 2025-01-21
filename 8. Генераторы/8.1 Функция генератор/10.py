def chunker(r, n):
    start, end = 0, n
    for _ in range(len(r) // n):
        yield r[start:end]
        start, end = end, end + n
    yield r[start:]
