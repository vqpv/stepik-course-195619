def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    lst = map(lambda x: x * 3, filter(lambda x: x % 3 == 0, nums))
    return tuple(lst)
