# boj 13549 숨바꼭질 3 g5
# noj.am/13549
import sys
from collections import deque

N, K = map(int, input().split())
visited = [sys.maxsize] * 100001  # 최소값을 찾기 위해, 범위가 <= 100000 이므로
dq = deque()
dq.append(N)
visited[N] = 0

while dq:  # bfs
    now = dq.popleft()
    # 다음 이동시간이 현재 저장되어 있는 시간보다 클 경우에 갱신
    if now - 1 > -1 and visited[now - 1] > visited[now] + 1:
        visited[now - 1] = visited[now] + 1
        dq.append(now - 1)
    if now + 1 < 100001 and visited[now + 1] > visited[now] + 1:
        visited[now + 1] = visited[now] + 1
        dq.append(now + 1)
    if now * 2 < 100001 and visited[now * 2] > visited[now]:
        visited[now * 2] = visited[now]
        dq.append(now * 2)

print(visited[K])
