# boj 14502 연구소 g5
# noj.am/14502
from itertools import combinations as cb
import copy
from collections import deque


def find_wall_and_virus():
    for i in range(len(laboratory)):
        for j in range(len(laboratory[0])):
            if laboratory[i][j] == 0:
                empty_list.append((i, j))
            elif laboratory[i][j] == 2:
                virus_list.append((i, j)) 


def bfs(*E): # 바이러스가 있는 위치에서 시작하여 bfs로 퍼트린다
    dq = deque([E])

    while dq:
        x, y = dq.popleft()
        visited[x][y] = True

        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < N and 0 <= Y < M and not visited[X][Y] and graph[X][Y] != 1:
                dq.append((X, Y))
                visited[X][Y] = True
                graph[X][Y] = 2


N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
empty_list = []
virus_list = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_safe_cnt = 0

find_wall_and_virus()

for (c1, c2, c3) in cb(empty_list, 3):
    visited = [[False] * M for _ in range(N)]
    graph = copy.deepcopy(laboratory)
    # 가능한 경우의 수를 모두 구하여 벽을 하나씩 세워본다
    graph[c1[0]][c1[1]] = 1
    graph[c2[0]][c2[1]] = 1
    graph[c3[0]][c3[1]] = 1

    for x, y in virus_list:
        bfs(x, y)
    
    cnt = 0
    for row in graph:
        for col in row:
            if col == 0:
                cnt += 1
    
    if cnt > max_safe_cnt:
        max_safe_cnt = cnt


print(max_safe_cnt)