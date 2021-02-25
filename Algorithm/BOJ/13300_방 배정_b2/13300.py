# boj 13300 방 배정 b2
# https://www.acmicpc.net/problem/13300
import math

N, K = map(int, input().split())
count_studentMen = [0] * 7  # 6학년까지 ex. 1학년은 1번인덱스를 사용
count_studentWomen = [0] * 7
res = 0

for i in range(N):
    S, Y = map(int, input().split())  # S성별 Y학년
    if S == 0:  # 여자라면
        count_studentWomen[Y] += 1  # 해당하는 학년의 여자수 증가
    else:
        count_studentMen[Y] += 1

for i in range(1, 7):  # 1~6학년까지 돌면서
    # 학년당 인원수 / 한방에 들어갈 수 있는 인원수 올림처리 ex. 2.3 일겨우 3개
    res += math.ceil(count_studentMen[i] / K)
    res += math.ceil(count_studentWomen[i] / K)

print(res)
