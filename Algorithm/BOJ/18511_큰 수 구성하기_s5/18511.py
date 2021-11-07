# boj 18511 큰 수 구성하기 s5
# noj.am/18511

from itertools import product as pd

def check_case(l):
    max_num = 0
    for case in pd(nums, repeat=l):
        num = int(''.join(map(str, case)))
        if num <= N:
            max_num = max(max_num, num)
    return max_num

N, K = map(int, input().split())
nums = list(map(int, input().split()))

ans = check_case(len(str(N))) # N의 자릿수만큼 K의 원소들을 활용하여 중복순열을 뽑아내서 비교 시도

if ans == 0: # 함수가 끝나도 최대값을 구하지 못했다면 자릿수 줄여서 다시 시도 ex. N = 177, K = 6, 9 -> 96(2자리)
    ans = check_case(len(str(N)) - 1)

print(ans)