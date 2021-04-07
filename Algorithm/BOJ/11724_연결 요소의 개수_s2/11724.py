# boj 11724 연결 요소의 개수 s2
# noj.am/11724

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = 0


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:  # dfs에 따라 연결이 되었으면 다 방문한다.
        ans += 1
        dfs(i)

print(ans)
