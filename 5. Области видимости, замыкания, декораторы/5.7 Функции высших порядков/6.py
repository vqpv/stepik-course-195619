def aggregation(func, sequence):
    result = [sequence[0]]
    for i in sequence[1:]:
        result.append(func(result[-1], i))
    return result[1:]
