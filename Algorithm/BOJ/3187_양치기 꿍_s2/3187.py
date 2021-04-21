# boj 3187 양치기 꿍 s2
# noj.am/3187
import sys
sys.setrecursionlimit(100000)

inp = sys.stdin.readline
R, C = map(int, inp().split())
graph = [inp().rstrip() for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * C for _ in range(R)]
res = {'v': 0, 'k': 0}


def dfs(x, y):
    global v, k
    visited[x][y] = True
    if graph[x][y] == 'v':  # 탐색 중 값이 v면 vcnt++
        v += 1
    elif graph[x][y] == 'k':  # 탐색 중 값이 k면 kcnt++
        k += 1
    for i in range(4):
        X, Y = x + dx[i], y + dy[i]
        # 범위를 벗어나지 않고 방문하지 않았고 울타리가 아닐 경우
        if 0 <= X < R and 0 <= Y < C and not visited[X][Y] and graph[X][Y] != '#':
            dfs(X, Y)


for i in range(R):
    for j in range(C):
        v, k = 0, 0
        if not visited[i][j] and graph[i][j] != '#':
            dfs(i, j)
            if v >= k:  # 늑대 수가 양의 수 이상이면 양이 다 잡아먹히므로 양은 0
                k = 0
            else:  # 양의 수가 늑대 수 초과면 늑대가 다 잡아먹히므로 늑대는 0
                v = 0
            res['v'] += v  # 사전에 값 추가
            res['k'] += k

print(res['k'], res['v'], sep=" ")
