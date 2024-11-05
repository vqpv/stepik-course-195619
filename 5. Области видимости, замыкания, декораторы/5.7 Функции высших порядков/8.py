def aggregation(func, sequence, initial=None):
    if initial:
        sequence.insert(0, initial)
    result = [sequence[0]]
    for i in sequence[1:]:
        result.append(func(result[-1], i))
    return result[-1]
