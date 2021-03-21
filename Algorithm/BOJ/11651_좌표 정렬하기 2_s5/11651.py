# boj 11651 좌표 정렬하기 2 s5
# noj.am/11651
import sys

inp = sys.stdin.readline
N = int(inp().rstrip())
coordinate = [list(map(int, inp().rstrip().split())) for _ in range(N)]
# y좌표순으로 정렬 후 같다면 x좌표순으로 정렬
res = sorted(coordinate, key=lambda x: (x[1], x[0]))

for i in range(N):  # 2차원 배열이므로 반복문을 통해 unpacking
    print(*res[i])
