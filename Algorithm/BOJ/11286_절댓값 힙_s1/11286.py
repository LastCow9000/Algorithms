# boj 11286 절댓값 힙 s1
# noj.am/11286
import heapq
import sys
from collections import deque

inp = sys.stdin.readline
N = int(inp())
hq = []

for _ in range(N):
    x = int(inp())
    if x == 0:
        if not hq:
            print(0)
            continue
        print(heapq.heappop(hq)[1])  # 실제 값 빼기
    else:
        heapq.heappush(hq, [abs(x), x])  # [절대값, 실제값]을 넣어 절대값 기준으로 정렬되게 함
