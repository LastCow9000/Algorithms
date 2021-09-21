# boj 2303 숫자 게임 s5
# noj.am/2303

N = int(input())
res = []
for i in range(N):
    nums = list(map(int, input().split()))
    maxVal = 0
    for j in range(len(nums) - 2):
        for k in range(j + 1, len(nums) - 1):
            for l in range(k + 1, len(nums)):
                tmp = (nums[j] + nums[k] + nums[l]) % 10
                if maxVal < tmp:
                    maxVal = tmp
    res.append((maxVal, i + 1))
# 완탐으로 일의 자리 최대값을 찾은 후 결과 리스트에서 값, 번호 순으로 최대값 뽑기
print(max(res, key=lambda x:(x[0], x[1]))[1])