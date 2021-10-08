# boj 13300 방 배정 b2
# https://www.acmicpc.net/problem/13300

import copy
from collections import deque


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
dq = deque()

def merge(x, y, dx, dy, board): # 어디서부터 채워넣을지, x y 변화량
    while dq:
        num = dq.popleft()
        if board[x][y] == 0: # 첫 값이면 바로 삽입
            board[x][y] = num

        elif board[x][y] == num: # 같으면 병합
            board[x][y] *= 2
            x += dx
            y += dy
        
        else: # 다르면 다음칸으로 이동 후 데이터 삽입
            x += dx
            y += dy
            board[x][y] = num


def move(d, board):
    if d == 0: # 상
        for j in range(N):
            for i in range(N):
                if board[i][j] > 0:
                    dq.append(board[i][j])
                    board[i][j] = 0
            
            merge(0, j, 1, 0, board) # 현재 열의 맨 꼭대기부터 한칸씩 내려오며 채움

    elif d == 1: # 하
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if board[i][j] > 0:
                    dq.append(board[i][j])
                    board[i][j] = 0
            
            merge(N - 1, j, -1, 0, board) # 현재 열의 맨 아래부터 한칸씩 올라오며 채움

    elif d == 2: # 좌
        for i in range(N):
            for j in range(N):
                if board[i][j] > 0:
                    dq.append(board[i][j])
                    board[i][j] = 0
            
            merge(i, 0, 0, 1, board)

    elif d == 3: # 우
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if board[i][j] > 0:
                    dq.append(board[i][j])
                    board[i][j] = 0
            
            merge(i, N - 1, 0, -1, board)


def solution(cnt, board):
    global max_val
    if cnt == 5:
        for row in board:
            max_val = max(max_val, max(row))
        return

    for i in range(4): # 상 하 좌 우 이동
        new_board = copy.deepcopy(board) # 원본 값 변화를 방지하기 위해 깊은 복사
        move(i, new_board)
        solution(cnt + 1, new_board) # 백트래킹

    return max_val

if __name__ == '__main__':
    print(solution(0, board))
