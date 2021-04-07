# boj 7569 토마토 s1
# noj.am/7569
import sys
from collections import deque

inp = sys.stdin.readline
M, N, H = map(int, inp().rstrip().split())
graph = [[list(map(int, inp().rstrip().split()))  # 3차원
          for _ in range(N)] for _ in range(H)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
date = 0


def check():  # 예외 체크를 위함
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    return True
    return False


dq = deque()
for i in range(H):  # 탐색시작지점 덱에 삽입
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                dq.append((i, j, k))

while dq and check():  # 탐색도 안했는데 0이 하나도 없을 경우(모두 익은 상황)에 0
    date += 1
    size = len(dq)
    for _ in range(size):  # 덱에 들어있는 사이즈만큼의 하루치
        x, y, z = dq.popleft()
        graph[x][y][z] = 1
        for i in range(6):
            X, Y, Z = x + dx[i], y + dy[i], z + dz[i]
            if -1 < X < H and -1 < Y < N and -1 < Z < M and graph[X][Y][Z] == 0:
                graph[X][Y][Z] = 1
                dq.append((X, Y, Z))

if check():
    print(-1)
else:
    print(date)
