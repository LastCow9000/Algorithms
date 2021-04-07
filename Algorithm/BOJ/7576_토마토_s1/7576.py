# boj 7576 토마토 s1
# noj.am/7576
import sys
from collections import deque

inp = sys.stdin.readline
M, N = map(int, inp().rstrip().split())
graph = [list(map(int, inp().rstrip().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
date = 0


def check():  # -1로 막혀서 못 익은 것과 처음부터 다 익어있는 상황 체크용
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return True
    return False


def bfs():
    global date
    dq = deque()
    for i in range(N):  # 탐색 시작점을 덱에 넣음
        for j in range(M):
            if graph[i][j] == 1:
                dq.append((i, j))

    while dq and check():  # 0이 존재하지 않는다면 탐색하지 않고 date는 변화가 없다(0)
        date += 1
        size = len(dq)
        for _ in range(size):  # 덱의 크기 만큼이 하루
            x, y = dq.popleft()
            for i in range(4):
                X, Y = x + dx[i], y + dy[i]
                if -1 < X < N and -1 < Y < M and graph[X][Y] == 0:
                    dq.append((X, Y))
                    graph[X][Y] = 1


bfs()

if check():  # 탐색을 하고도 0이 존재한다면 다 익지 못한것.
    print(-1)

else:
    print(date)
