# boj 2108 통계학 s4
# noj.am/2108

import sys
from collections import Counter

inp = sys.stdin.readline
N = int(inp().rstrip())
integers = [int(inp().rstrip()) for _ in range(N)]
integers.sort()  # 중앙값 계산을 위한 정렬


def maxFreq(_list):  # 라이브러리 사용
    cnt = Counter(_list)
    res = cnt.most_common(2)  # 최빈값 상위 2개 구하기
    return res[1][0] if len(res) > 1 and res[0][1] == res[1][1] else res[0][0]


'''
def maxFreq(_list):  # 최빈값 구하기
    dict = {}
    for integer in _list:
        dict.setdefault(integer, 0)  # 해당 키값의 값이 있다면 값, 없다면 0으로 초기화
        dict[integer] += 1
    res = [k for k, v in dict.items() if v == max(
        dict.values())]  # 사전 값의 최대 값과 동일한 키만 리스트로 만듬
    res.sort()
    # 키 값이 담긴 리스트의 길이가 2 이상 일 경우(max값이 2개이상 존재할 경우) 두번째로 작은 값 리턴
    return res[1] if len(res) > 1 else res[0]
'''

print("%.f" % (sum(integers) / N))
print(integers[len(integers) // 2])
print(maxFreq(integers))
print(integers[-1] - integers[0])
