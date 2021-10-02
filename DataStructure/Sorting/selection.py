# O(N^2)
# Unstable

nums = list(map(int, input().split()))

for i in range(len(nums)):
    min_val = nums[i]
    min_idx = i
    for j in range(i, len(nums)):
        if nums[j] < min_val:
            min_val = nums[j]
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(nums)