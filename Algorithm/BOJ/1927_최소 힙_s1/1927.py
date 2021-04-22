# boj 1927 최소 힙 s1
# noj.am/1927
import sys
import heapq

inp = sys.stdin.readline
N = int(inp())
_list = []
heapq.heapify(_list)

for _ in range(N):
    x = int(inp())
    if x > 0:
        heapq.heappush(_list, x)
    else:
        if len(_list) == 0:
            print(0)
        else:
            print(heapq.heappop(_list))
