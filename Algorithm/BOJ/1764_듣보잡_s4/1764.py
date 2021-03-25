# boj 1764 듣보잡 s4
# noj.am/1764

# 이분탐색으로 풀이
import sys

inp = sys.stdin.readline
N, M = map(int, inp().rstrip().split())
cantHear = [inp().rstrip() for _ in range(N)]
cantHear.sort()  # 이분탐색을 위한 정렬
cantSee = [inp().rstrip() for _ in range(M)]
res = []


def binarySearch(target):
    left = 0
    right = len(cantHear) - 1

    while left < right:
        mid = (left + right) // 2
        if cantHear[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if cantHear[left] == target:  # 찾는 값이 존재하면 리스트에 추가
        res.append(target)


for i in cantSee:
    binarySearch(i)
print(len(res))
res.sort()  # 사전순 정렬
print('\n'.join(res))  # unpacking
