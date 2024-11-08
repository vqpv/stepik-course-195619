def create_accumulator():
    nums = []
    def inner(x):
        nums.append(x)
        return sum(nums)
    return inner
