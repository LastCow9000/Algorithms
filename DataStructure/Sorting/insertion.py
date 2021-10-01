# O(N^2)
# Stable

nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    tmp = nums[i]
    idx = i - 1 # 현재 인덱스의 왼쪽만 봄

    # 인덱스를 감소시켜가면서 tmp 보다 작은 수 탐색(있다면 뒤로 당김)
    while 0 <= idx and tmp < nums[idx]: 
        nums[idx + 1] = nums[idx]
        idx -= 1
    
    nums[idx + 1] = tmp # 위에서 tmp보다 큰 수를 만났거나 인덱스가 음수여서 끝났으므로 + 1


print(nums)