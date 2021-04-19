# boj 1325 효율적인 해킹 s2
# noj.am/1325
import collections
import sys
from collections import deque

inp = sys.stdin.readline
N, M = map(int, inp().split())
computers = [[] for _ in range(N + 1)]
ans = {}

for i in range(M):  # 단방향 그래프 입력
    A, B = map(int, inp().split())
    computers[B].append(A)


def bfs(x):
    global cnt
    dq = deque()
    dq.append(x)
    visited[x] = True

    while dq:
        node = dq.popleft()
        for i in computers[node]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True
                cnt += 1  # 탐색할 때마다 +1씩


for i in range(1, N + 1):  # 모든 정점에서 출발해봄
    visited = [False] * (N + 1)
    cnt = 0
    bfs(i)
    ans[i] = cnt

res = [k for k, v in ans.items() if v == max(
    ans.values())]  # 사전에서 value가 최대값인 것만 리스트화
print(*sorted(res))


''' dfs 메모리초과 
sys.setrecursionlimit(10001)

inp = sys.stdin.readline
N, M = map(int, inp().split())
computers = [[] for _ in range(N + 1)]
ans = {}

for i in range(M):  # 단방향 그래프 입력
    A, B = map(int, inp().split())
    computers[B].append(A)


def dfs(x):
    global cnt
    visited[x] = True
    for node in computers[x]:
        if not visited[node]:
            cnt += 1  # 탐색할 때마다 +1씩
            dfs(node)


for i in range(1, N + 1):  # 모든 정점에서 출발해봄
    visited = [False] * (N + 1)
    cnt = 0
    dfs(i)
    ans[i] = cnt


res = [k for k, v in ans.items() if v == max(ans.values())]  # 사전에서 value가 최대값인 것만 리스트화
print(*sorted(res))
'''
