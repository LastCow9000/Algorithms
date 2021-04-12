# boj 1758 알바생 강호 s4
# noj.am/1758
import sys

inp = sys.stdin.readline
N = int(inp())
tips = [int(inp()) for _ in range(N)]
tips.sort(reverse=True)  # 주려고 하는 돈이 큰게 앞에 올수록 팁을 많이 받는다
maxTip = 0

for i in range(1, N + 1):
    tip = tips[i - 1] - (i - 1)
    if tip >= 0:
        maxTip += tip

print(maxTip)
