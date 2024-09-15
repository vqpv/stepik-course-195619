def my_func(collection, n):
    result = collection.copy()
    for i in range(1, n + 1):
        result.append(i)
    return result
