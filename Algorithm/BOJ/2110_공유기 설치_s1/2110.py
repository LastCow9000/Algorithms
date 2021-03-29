# boj 2110 공유기 설치 s1
# noj.am/2110

import sys

inp = sys.stdin.readline
N, C = map(int, inp().rstrip().split())
home = [int(inp().rstrip()) for _ in range(N)]
home.sort()


def routerCnt(distance):
    idx = 0
    cnt = 1  # 설치한 공유기 개수, 1번집은 무조건 설치
    for i in range(N):
        if home[i] - home[idx] >= distance:  # 각 집의 거리차가 distance보다 크면 공유기 설치 가능
            cnt += 1
            idx = i
    return cnt


def parametricSearch(target):
    left = 1
    right = int(1e9)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if routerCnt(mid) >= target:  # 원하는 갯수가 설치되었으면
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    return ans


print(parametricSearch(C))
