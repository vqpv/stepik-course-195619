def get_arith_progression(a1, d, n):
    if n == 1:
        return a1
    return get_arith_progression(a1, d, n - 1) + d
