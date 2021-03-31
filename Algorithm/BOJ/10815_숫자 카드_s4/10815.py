# boj 10815 숫자 카드 s4
# noj.am/10815

import sys

inp = sys.stdin.readline
N = int(inp().rstrip())
cardList = list(map(int, inp().rstrip().split()))
cardList.sort()  # 이분탐색을 위한 정렬
M = int(inp().rstrip())
targetList = list(map(int, inp().rstrip().split()))
res = []


def checkCard(target):
    left = 0
    right = len(cardList) - 1
    while left < right:
        mid = (left + right) // 2
        if cardList[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return 1 if target == cardList[(left + right) // 2] else 0


for target in targetList:
    res.append(checkCard(target))

print(*res)
