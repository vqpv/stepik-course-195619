def count_calls():
    total_calls = 0
    def inner():
        nonlocal total_calls
        total_calls += 1
        inner.total_calls = total_calls
        return total_calls
    inner.total_calls = total_calls
    return inner
