def power(a: int, n: int) -> int:
        if n == 1:
            return a
        else:
            return power(a, n - 1) * a
