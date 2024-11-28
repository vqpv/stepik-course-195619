def multiply_result_by(N):
    def decorator(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * N
        return inner
    return decorator
