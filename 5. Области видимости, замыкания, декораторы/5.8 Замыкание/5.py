def countdown(count):
    nums = [1] * count
    def inner():
        if nums:
            print(len(nums))
            nums.pop()
        else:
            print(f"Превышен лимит, вы вызвали более {count} раз")
    return inner
