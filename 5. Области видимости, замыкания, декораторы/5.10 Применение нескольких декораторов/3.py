def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return [i.upper() if isinstance(i, str) else i for i in res]
        elif isinstance(res, dict):
            return dict(map(lambda x: (x[0].upper(), x[1]) if isinstance(x[0], str) else (x[0], x[1]), res.items()))
    return wrapper
