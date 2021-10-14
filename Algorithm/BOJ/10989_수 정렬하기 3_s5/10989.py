# boj 10989 수 정렬하기 s5
# noj.am/10989
import sys; r = sys.stdin.readline

N = int(r())
cnt_arr = [0] * 10_001
for _ in range(N):
    cnt_arr[int(r())] += 1

for idx, num in enumerate(cnt_arr):
    if num > 0:
        for _ in range(num):
            print(idx)

# num_cnt = {}
# for _ in range(N):
#     n = int(input())
#     num_cnt[n] = num_cnt.setdefault(n, 0) + 1

# ans = sorted(num_cnt.items())
# for k, cnt in ans:
#     for _ in range(cnt):
#         print(k)