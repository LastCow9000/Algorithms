# boj 21921 블로그 s3
# noj.am/21921

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

prefixSum = [0]
for i in range(N): # 슬라이딩 윈도우로 합을 구하기 위해 구간 합을 구함
    prefixSum.append(prefixSum[i] + visitors[i])

left = 0
right = X - 1
cnt = 0
maxDay = 0

while right <= N: # 슬라이딩 윈도우 종료 조건
    slidingWindow = prefixSum[right] - prefixSum[left - 1]
    if slidingWindow > maxDay:
        maxDay = slidingWindow
        cnt = 1 # 최대값이 갱신되면 1로 갱신
    elif slidingWindow == maxDay: # 최대값이 같은 날이 나오면 ++
        cnt += 1
    left += 1
    right += 1

print("SAD") if maxDay == 0 else print(maxDay, cnt, sep="\n")