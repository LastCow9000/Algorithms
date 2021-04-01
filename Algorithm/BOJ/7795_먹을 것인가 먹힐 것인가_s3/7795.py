# boj 7795 먹을 것인가 먹힐 것인가 s3
# noj.am/7795
import sys
import bisect

inp = sys.stdin.readline
T = int(input())


def binarySearch(A, target):
    upperBound = bisect.bisect_right(A, target)
    # A의 갯수에서 b의 원소가 A의 값중에서 초과하는 인덱스(upper bound)를 빼주면 된다
    return len(A) - upperBound


for _ in range(T):
    ans = 0
    N, M = map(int, input().split())
    A = list(map(int, inp().rstrip().split()))
    B = list(map(int, inp().rstrip().split()))

    A.sort()
    for b in B:
        ans += binarySearch(A, b)

    print(ans)
