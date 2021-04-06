# boj 1260 DFS와 BFS s2
# noj.am/1260
from collections import deque
import sys

inp = sys.stdin.readline
N, M, V = map(int, inp().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):  # 그래프 입력 받기
    x, y = map(int, inp().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N + 1):  # 정점의 번호가 낮은 것부터 탐색을 위함
    graph[i].sort()

dfsList = []  # 탐색 결과 저장용
bfsList = []


def dfs(x):
    visited[x] = True
    dfsList.append(x)
    for next in graph[x]:
        if not visited[next]:
            dfs(next)


def bfs():
    dq = deque()
    visited[V] = True
    dq.append(V)
    bfsList.append(V)

    while dq:
        node = dq.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                dq.append(next)
                bfsList.append(next)


dfs(V)
visited = [False for _ in range(N + 1)]  # dfs에서 썼으므로 다시 처음값으로 초기화
bfs()

print(*dfsList)
print(*bfsList)
