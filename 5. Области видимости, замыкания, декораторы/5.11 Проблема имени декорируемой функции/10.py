def cache_result(func):
    cache = {}
    def inner(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache: 
            print(f"[FROM CACHE] Вызов {func.__name__} = {cache[key]}")
            return cache[key]
        else:
            result = func(*args, **kwargs) 
            cache[key] = result
            return result
    inner.__name__ = func.__name__
    return inner
