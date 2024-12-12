def filter_numbers(nums):
    return list(filter(lambda x: x % 2 == 0 or abs(x) > 100, nums))
