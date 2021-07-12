# boj 1753 최단경로 g5
# noj.am/1753
import sys; inp = sys.stdin.readline
import heapq


V, E = map(int, inp().split())
start = int(inp())

graph = [[] for _ in range(V + 1)]
INF = 1000000 # 최대값은 20만정도 나오는데 넉넉하고 안전하게 백만
dist = [INF for _ in range(V + 1)] # 0이 아니라 1부터 시작하므로

for _ in range(E):
    u, v, w = map(int, inp().split())
    graph[u].append((v, w)) # u -> v 로 가는 가중치 w

def dijkstra(start):
    pq = [(0, start)] # 시작 점의 가중치는 0
    dist[start] = 0

    while pq:
        dis, next = heapq.heappop(pq)
        # pq에서 뽑은 값에서 기존 vertex(next)의 거리(최소값)보다 가중치가 더 큰 경우 
        # 최소거리를 구하는 것이기 때문에 무시
        if dis > dist[next]: 
            continue

        for nextNode, nextDist in graph[next]:
            if dist[nextNode] > nextDist + dis: # 최소거리 갱신
                dist[nextNode] = nextDist + dis
                heapq.heappush(pq, (dist[nextNode], nextNode))


dijkstra(start)
print(*['INF' if dist[i] == INF else dist[i] for i in range(1, len(dist))], sep="\n") 