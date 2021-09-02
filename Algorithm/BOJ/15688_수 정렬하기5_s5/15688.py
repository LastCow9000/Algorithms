# boj 15688 수 정렬하기 5 s5
# noj.am/15688
import sys; inp = sys.stdin.readline

cnt_nums = [0] * 2000001
# 계수 정렬
for _ in range(int(inp())):
    cnt_nums[int(inp()) + 1000000] += 1

for i in range(len(cnt_nums)):
    while cnt_nums[i] > 0:
        print(i - 1000000)
        cnt_nums[i] -= 1