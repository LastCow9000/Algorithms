# boj 11663 선분 위의 점 s3
# noj.am/11663

import bisect
import sys

inp = sys.stdin.readline
N, M = map(int, inp().rstrip().split())
dots = list(map(int, inp().rstrip().split()))
dots.sort()
lines = [list(map(int, inp().rstrip().split())) for _ in range(M)]


def binarySearch(s, e):  # 점 들중에서 선분이 끝나는 부분을 초과하는 인덱스 - 선분이 시작하는 부분의 첫 인덱스
    lowerBound = bisect.bisect_left(dots, s)
    upperBound = bisect.bisect_right(dots, e)
    return upperBound - lowerBound


for s, e in lines:
    print(binarySearch(s, e))
