def create_accumulator(num=0):
    nums = [num]
    def inner(x):
        nums.append(x)
        return sum(nums)
    return inner
