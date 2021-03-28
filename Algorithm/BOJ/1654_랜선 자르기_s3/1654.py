# boj 1654 랜선 자르기 s3
# noj.am/1654

# parametric search

import sys

inp = sys.stdin.readline
K, N = map(int, inp().rstrip().split())
lines = [int(inp().rstrip()) for _ in range(K)]


def cnt(length):  # 길이에 따른 랜선 갯수 구하기
    res = 0
    for line in lines:
        res += line // length
    return res


def binarySearch(target):
    left = 0
    right = 2 ** 31 - 1
    ans = 0

    while left <= right:  # 같을 때도 돌아서 테스팅해야 함
        mid = (left + right) // 2
        if cnt(mid) < target:  # 원하는 갯수를 못 만들면 길이를 조금 줄여보자!(right--)
            right = mid - 1
        else:
            left = mid + 1  # 원하는 갯수 이상 만들 수 있으면 길이를 늘려보자(left++)
            ans = max(mid, ans)
    return ans


print(binarySearch(N))
