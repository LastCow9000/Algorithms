# boj 11659 구간 합 구하기 4 s3
# noj.am/11659
import sys

inp = sys.stdin.readline
N, M = map(int, inp().rstrip().split())
_list = list(map(int, inp().rstrip().split()))
prefixSum = [0]  # 구간 합의 첫 원소를 0으로.
# 1번째 값 [pre[0] - pre[-1]]을 [pre[1] - pre[0]]으로 변경

for i in range(N):
    prefixSum.append(prefixSum[i] + _list[i])  # 누적합 = 전 번째 원소 + 현 원소

for i in range(M):
    x, y = map(int, inp().rstrip().split())
    # N ~ M의 합은 (1 ~ M의 합 - 1 ~ N-1의 합)
    print(prefixSum[y] - prefixSum[x - 1])
