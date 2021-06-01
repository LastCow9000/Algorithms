# boj 1978 소수 찾기 s4
# noj.am/1978

_ = int(input())
nums = set(map(int, input().split()))
prime = set()
maxVal = max(nums)
flag = [False, False] + [True] * (maxVal - 1)

# 에라토스테네스의 체
for num in range(2, maxVal + 1):
    if flag[num]:
        prime.add(num)
        for i in range(num, maxVal + 1, num):
            flag[i] = False

print(len(nums & prime)) # 교집합 후 갯수
