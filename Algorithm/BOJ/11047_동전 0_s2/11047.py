# boj 11047 동전 0 s2
# noj.am/11047

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N - 1, -1, -1):  # 큰 동전부터 나누어본다
    if K // A[i] >= 1:
        cnt += K // A[i]
        K %= A[i]

print(cnt)
