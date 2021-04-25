# boj 16918 봄버맨 s1
# noj.am.16918
import sys
from collections import deque

inp = sys.stdin.readline
R, C, N = map(int, inp().split())
grid = [list(inp().rstrip()) for _ in range(R)]
bombLoc = deque()
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def whichBomb():
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "O":  # 폭탄이 있는 위치 찾기
                bombLoc.append((i, j))


def setupBomb():
    global grid
    grid = [["O"] * C for _ in range(R)]


def bomb():
    while bombLoc:
        x, y = bombLoc.popleft()
        grid[x][y] = "."
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < R and 0 <= Y < C:
                grid[X][Y] = "."


N -= 1  # 처음 1초후는 변화 없음
while N > 0:
    whichBomb()
    setupBomb()
    N -= 1  # 2차로 폭탄 설치 후 1초가 지나야 터짐
    if N == 0:
        break
    bomb()
    N -= 1  # 시간 흐름

for arr in grid:  # 결과 출력
    print("".join(arr))
