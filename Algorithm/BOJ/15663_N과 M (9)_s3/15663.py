# boj 16663 N과 M (9) s3
# noj.am/15663
import itertools

N, M = map(int, input().split())
_list = list(list(map(int, input().split())))
ans = itertools.permutations(_list, M)
ans = sorted(list(set(ans)))

for i in ans:
    print(*i)
