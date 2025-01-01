def get_combin(n, k):
    if k == 0 or k == n:
        return 1
    elif 0 < k < n:
        return get_combin(n - 1, k) + get_combin(n - 1, k - 1)
