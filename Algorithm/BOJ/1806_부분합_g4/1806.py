# boj 1806 부분합 g4
# noj.am/1806
import sys

inp = sys.stdin.readline
N, S = map(int, inp().split())
_list = list(map(int, inp().split()))

minVal = int(1e5)

prefixSum = [0]
for i in range(N):  # 구간 합 리스트
    prefixSum.append(prefixSum[i] + _list[i])

left = 0
right = 0
while right < N + 1:  # right가 prefixsum 배열 마지막 인덱스보다 밖이면 stop, 초기값0 때문에 +1
    tmp = prefixSum[right] - prefixSum[left]
    if tmp >= S:
        minVal = min(minVal, right - left)

    if tmp < S:  # 합과 S의 관계에 따라 포인터 이동
        right += 1
    else:
        left += 1

print(0) if minVal == int(1e5) else print(minVal)
