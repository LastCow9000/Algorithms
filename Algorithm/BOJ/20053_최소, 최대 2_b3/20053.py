# boj 20053 최소, 최대 2 b3
# noj.am/20053
import sys; inp = sys.stdin.readline

for _ in range(int(input())):
    N = int(inp())
    _list = list(map(int, inp().split()))
    minValue = 1000001
    maxValue = -1000001

    for num in _list:
        if num >= maxValue:
            maxValue = num
        if num <= minValue:
            minValue = num
    
    print(minValue, maxValue, sep=" ")