# boj 17276 배열 돌리기 s2
# noj.am/17276
import sys

inp = sys.stdin.readline
T = int(inp())

for _ in range(T):
    n, d = map(int, inp().split())
    arrs = [list(map(int, inp().split())) for _ in range(n)]
    if d > 0:  # 양의 각도
        d //= 45  # 45도로 나눈 만큼 회전 반복
        for _ in range(d):
            priDiagonal = []
            midCol = []
            subDiagonal = []
            midRow = []
            for i in range(n):  # 주대각선, 가운데 열 등을 뽑아냄
                priDiagonal.append(arrs[i][i])
                midCol.append(arrs[i][n // 2])
                subDiagonal.append(arrs[n - i - 1][i])
                midRow.append(arrs[n // 2][i])
            for i in range(n):  # 뽑아낸 값을 이용하여 변경
                arrs[i][n // 2] = priDiagonal[i]
                arrs[n - i - 1][i] = midCol[-(i + 1)]
                arrs[n // 2][i] = subDiagonal[i]
                arrs[i][i] = midRow[i]
    elif d < 0:
        d = abs(d) // 45
        for _ in range(d):
            priDiagonal = []
            midCol = []
            subDiagonal = []
            midRow = []
            for i in range(n):
                priDiagonal.append(arrs[i][i])
                midCol.append(arrs[i][n // 2])
                subDiagonal.append(arrs[n - i - 1][i])
                midRow.append(arrs[n // 2][i])
            for i in range(n):
                arrs[n // 2][i] = priDiagonal[i]
                arrs[n - i - 1][i] = midRow[i]
                arrs[i][n // 2] = subDiagonal[-(i + 1)]
                arrs[i][i] = midCol[i]
    for arr in arrs:
        print(*arr)
