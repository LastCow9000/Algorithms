# boj 10814 나이순 정렬 s5
# noj.am/10814
import sys

inp = sys.stdin.readline
N = int(inp().rstrip())
members = [list(inp().rstrip().split()) for _ in range(N)]
res = sorted(members, key=lambda x: int(x[0]))  # 나이순으로 정렬

for i in range(N):  # 2차원 배열이므로 반복문을 통해서 unpacking
    print(*res[i])
