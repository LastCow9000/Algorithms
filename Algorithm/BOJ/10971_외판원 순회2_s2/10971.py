# boj 10971 외판원 순회 2 s2
# noj.am/10971

import sys
import itertools

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
res = sys.maxsize


def sol(r):
    ans = 0
    for i in range(N - 1):
        if W[r[i]][r[i + 1]] != 0:
            # ex) N이 4, r = [0, 1, 2, 3] 일때 0 1 -> 1 2 -> 2 3
            ans += W[r[i]][r[i + 1]]
        else:
            return sys.maxsize
    if W[r[-1]][r[0]] != 0:
        ans += W[r[-1]][r[0]]  # ex) 3 -> 0
    else:
        return sys.maxsize
    return ans


for perm in itertools.permutations(range(N)):  # 순회루트를 순열로 다 구해서 탐색해본다
    res = min(res, sol(perm))

print(res)

'''
# 직접 구현
import sys

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize


def dfs(start, next, res, visited):
    global ans
    if len(visited) == N:  # 다 방문했으면
        if W[next][start] != 0:  # 다시 처음으로 돌아갈 수 있으면
            ans = min(ans, res + W[next][start])
        return

    for i in range(N):  # 0부터 탐색
        # 시작 도시가 아니고 갈 수 있고 방문한 도시가 아니라면
        if start != i and W[next][i] != 0 and i not in visited:
            visited.append(i)
            dfs(start, i, res + W[next][i], visited)
            visited.pop()  # 백트래킹


for i in range(N):
    dfs(i, i, 0, [i])  # 시작, 다음탐색깊이, 결과값, 방문한 인덱스

print(ans)

'''
