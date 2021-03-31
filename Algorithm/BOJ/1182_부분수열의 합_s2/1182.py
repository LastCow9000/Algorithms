# boj 1182 부분수열의 합 s2
# noj.am/1182

import itertools

N, S = map(int, input().split())
_int = list(map(int, input().split()))

# 라이브러리 사용
cnt = 0

for i in range(1, N + 1):
    for comb in itertools.combinations(_int, i):
        if sum(comb) == S:
            cnt += 1


# 직접 구현해보기
