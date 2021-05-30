# boj 2960 에라토스테네스의 체 s4
# noj.am/2960

N, K = map(int, input().split())

visited = [False, False] + [True] * (N - 1)
cnt = 0

for i in range(2, N + 1):
    if visited[i]:
        for j in range(i, N + 1 ,i):
            if visited[j]:
                cnt += 1
            visited[j] = False
            if cnt == K:
                print(j)
                break