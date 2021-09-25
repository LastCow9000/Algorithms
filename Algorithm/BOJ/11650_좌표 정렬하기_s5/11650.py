# boj 11650 좌표 정렬하기 s5
# noj.am/11650
import sys; r = sys.stdin.readline

N = int(r())
pos_list = [list(map(int, r().split())) for _ in range(N)]
pos_list.sort(key=lambda x:(x[0], x[1]))
for pos in pos_list:
    print(*pos)