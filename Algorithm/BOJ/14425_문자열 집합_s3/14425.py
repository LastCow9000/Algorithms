# boj 14425 문자열 집합 s3
from sys import stdin

_input = stdin.readline
N, M = map(int, _input().rstrip().split())
S = {_input().rstrip() for _ in range(N)}  # S를 입력받아서 set으로 구성
cnt = 0

for _ in range(M):
    if _input().rstrip() in S:  # 입력받은 값이 S에 있다면 cnt++
        cnt += 1

print(cnt)
