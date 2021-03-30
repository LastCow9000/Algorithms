# boj 10974 모든 순열 s3
# noj.am/10974

N = int(input())


def recursive(_list):
    if len(_list) == N:
        print(*_list)

    for i in range(1, N + 1):
        if i not in _list:
            _list.append(i)
            recursive(_list)
            _list.pop()


recursive([])

''' 라이브러리 사용
import itertools

N = int(input())
res = itertools.permutations(range(1, N + 1), N)
for data in res:
    print(' '.join(map(str, data)))
'''

'''
# 인덱스로
N = int(input())
_list = []


def recursive(idx):
    if idx == N:
        print(*_list)

    for i in range(1, N + 1):
        if i not in _list:
            _list.append(i)
            recursive(idx + 1)
            _list.pop()


recursive(0)
'''
