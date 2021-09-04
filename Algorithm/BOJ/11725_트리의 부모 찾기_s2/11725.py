# boj 11725 트리의 부모 찾기 s2
# noj.am/11725
import sys
sys.setrecursionlimit(int(1e6))

N = int(input())
tree = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)

for _ in range(N - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(V):
    for node in tree[V]:
        if node == parents[V]:
            continue
        parents[node] = V
        dfs(node) 

dfs(1)

print(*parents[2:], sep='\n')
