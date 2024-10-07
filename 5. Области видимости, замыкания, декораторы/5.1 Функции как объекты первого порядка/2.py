f_cache = {}

def factorial(n):
    if n in f_cache:
        print(f"Get from cache value factorial({n})")
        return f_cache[n]
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        f_cache[n] = result
        return result
