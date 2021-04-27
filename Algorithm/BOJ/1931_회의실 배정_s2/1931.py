# boj 1931 회의실 배정 s2
# noj.am/1931
import sys

inp = sys.stdin.readline
N = int(inp())
times = [list(map(int, inp().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))
prev_end = 0
cnt = 0

for start, end in times:
    if start >= prev_end:
        prev_end = end
        cnt += 1

print(cnt)
