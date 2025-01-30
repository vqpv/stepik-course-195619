def get_average():
    nums = []
    result = 0
    while True:
        n = yield result
        nums.append(n)
        result = sum(nums) / len(nums)
