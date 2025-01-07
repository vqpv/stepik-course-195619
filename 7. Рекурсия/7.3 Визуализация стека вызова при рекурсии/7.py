def quick_power(a, n):
    print(f"State: a={a}, n={n}")
    if n == 0:
        return 1
    if n % 2 == 0:
        return quick_power(a, n // 2) ** 2
    else:
        return quick_power(a, n - 1) * a
