# boj 9372 상근이의 여행 s4
# noj.am/9372

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    print(N - 1) # 트리에서 간선의 개수는 정점의 갯수 - 1