# boj 16926 배열 돌리기 1 s3
# noj.am/16926
import sys

inp = sys.stdin.readline
N, M, R = map(int, inp().split())
A = [list(map(int, inp().split())) for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]  # ↓ → ↑ ←
position = min(N, M) // 2  # 몇개의 그룹을 돌려야하는지


def rotate(position):
    for i in range(position):
        direction = 0
        x, y = i, i
        start = A[x][y]  # 나중에 값 갱신을 위해 처음 시작 위치 저장

        while direction < 4:  # 4방향
            Y, X = y + dy[direction], x + dx[direction]
            if i <= Y < M - i and i <= X < N - i:  # 도는 범위가 맞으면 돈다
                A[x][y] = A[X][Y]
                x = X
                y = Y
            else:
                direction += 1  # 한 쪽 방향을 다돌았으면 방향 회전
        A[i + 1][i] = start  # 처음 값이 덮어씌워져서 갱신


for _ in range(R):
    rotate(position)

for arr in A:
    print(*arr)
