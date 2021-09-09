# boj 20165 인내의 도미노 장인 호석 g5
# noj.am/20165
import sys; r = sys.stdin.readline
import copy

N, M, R = map(int, r().split())
board = [list(map(int, r().split())) for _ in range(N)]
res_board = copy.deepcopy(board)
ans = 0

def attack(x, y, d, cnt): # cnt 넘어뜨릴 갯수
    global ans
    dir = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}

    if res_board[x][y] >= cnt: # 현재 넘어뜨려야 할 갯수보다 현재 도미노 높이가 크다면 갱신
        cnt = res_board[x][y]

    if res_board[x][y] != -1: # 도미노가 서있다면
        res_board[x][y] = -1 # 넘어뜨린다
        ans += 1 # 넘어뜨린 갯수
    cnt -= 1

    nx = x + dir[d][0]
    ny = y + dir[d][1]

    if 0 <= nx < N and 0 <= ny < M and cnt > 0: # 범위안에 있고 넘어뜨릴 갯수가 남아있다면
        attack(nx, ny, d, cnt)


def defence(x, y):
    if res_board[x][y] == -1: # 도미노가 넘어져있다면
        res_board[x][y] = board[x][y] # 복구한다


def change_res():
    for i in range(len(res_board)):
        for j in range(len(res_board[0])):
            if res_board[i][j] == -1:
                res_board[i][j] = 'F'
            else:
                res_board[i][j] = 'S'


def solution():
    for _ in range(R):
        ax, ay, ad = r().split()
        ax, ay = int(ax), int(ay)
        dx, dy = map(int, r().split())
        attack(ax - 1, ay - 1, ad, 0)
        defence(dx - 1, dy - 1)

    change_res()

    print(ans)
    for row in res_board:
        print(*row)


if __name__ == "__main__":
    solution()