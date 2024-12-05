nums = list(map(int, input().split()))

print(all((nums[i] > nums[i + 1] for i in range(len(nums) - 1))))
