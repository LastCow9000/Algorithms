# boj 1913 달팽이 s5
# noj.am/1913

N = int(input())
find_num = int(input())
board = [[0] * (N + 2) for _ in range(N + 2)]

# 테두리에 가벽을 세운다
for i in range(N + 1):
    board[0][i] = 1
    board[N + 1][i] = 1
    board[i][0] = 1
    board[i][N + 1] = 1

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cur_dir = 0

x, y = 1, 1
ans = []

for i in range((N ** 2), 0, -1):
    test_x, test_y = x + dx[cur_dir], y + dy[cur_dir] 
    board[x][y] = i
    if i == find_num:
        ans = [x, y]

    # 가벽을 만나거나 이미 숫자가 들어있으면(0이 아니면) 방향 전환
    if board[test_x][test_y]:    
        cur_dir = (cur_dir + 1) % 4

    x, y = x + dx[cur_dir], y + dy[cur_dir]

# 가벽 제외하고 출력
for i in range(1, N + 1):
    print(*board[i][1:N + 1])
print(*ans)