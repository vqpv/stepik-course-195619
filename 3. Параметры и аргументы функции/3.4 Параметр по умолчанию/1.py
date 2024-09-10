def product(nums, start=1):
    result = start
    for i in nums:
        result *= i
    return result
