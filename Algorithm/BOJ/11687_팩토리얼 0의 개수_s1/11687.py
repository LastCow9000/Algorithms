# boj 11687 팩토리얼 0의 개수 s1
# noj.am/11687
import sys

M = int(input())


def cnt(val):  # 5 * 2를 해야 0이 늘어나므로 5의 개수가 0의 개수와 같다
    res = 0
    while val > 4:
        res += val // 5
        val = val // 5
    return res


def binarySearch(target):
    left = 0
    right = sys.maxsize
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if cnt(mid) >= target:
            right = mid - 1
            ans = mid
        else:
            left = mid + 1

    return ans if cnt(ans) == target else -1


print(binarySearch(M))
