# boj 2231 분해합 b2
# noj.am/2231
from collections import defaultdict


N = input()
res = defaultdict(list)

for i in range(1, 1_000_001):
    tmp = sum(list(map(int, str(i)))) + i
    res[str(tmp)].append(i)

ans = res[N]
print(min(ans)) if ans else print(0)
