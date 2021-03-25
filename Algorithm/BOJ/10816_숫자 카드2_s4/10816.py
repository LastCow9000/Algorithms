# boj 10816 숫자 카드 2 s4
# noj.am/10816

import sys
import bisect

inp = sys.stdin.readline
N = int(inp().rstrip())
cards = list(map(int, inp().rstrip().split()))
cards.sort()  # 이분탐색을 위한 정렬
M = int(inp().rstrip())
nums = list(map(int, inp().rstrip().split()))

# 아래 코드 한줄로
print(*[bisect.bisect_right(cards, i) - bisect.bisect_left(cards, i)
        for i in nums])
'''
for i in nums:
    lowerbound = bisect.bisect_left(cards, i)
    upperbound = bisect.bisect_right(cards, i)
    print(upperbound - lowerbound, end=" ")
'''
