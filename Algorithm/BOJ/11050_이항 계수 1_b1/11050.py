# boj 11050 이항 계수 1 b5
# noj.am/11050

def solution(n, k):
    if k == 0 or k == n:
        return 1
    if not dp[n][k]:
        dp[n][k] = solution(n - 1, k - 1) + solution(n - 1, k)
    return dp[n][k]

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
print(solution(N, K))