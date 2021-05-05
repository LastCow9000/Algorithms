# boj 11279 최대 힙 s2
# noj.am/11279
import heapq
import sys

inp = sys.stdin.readline
N = int(inp())
pq = []

for i in range(N):
    num = int(inp())
    if num == 0:
        if not pq:  # pq가 비었는데 0이 입력되면 0출력
            print(0)
        else:
            print(-heapq.heappop(pq))  # 파이썬 heap은 최소힙이라서 최대힙을 만들어주기 위해 음수로 넣어줌
    else:
        heapq.heappush(pq, -num)  # 음수의 제일 작은 값 -> 양수로 바꿨을 시 제일 큰 값
