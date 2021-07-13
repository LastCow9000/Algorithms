# boj 1504 특정한 최단경로 g4
# noj.am/1504
import sys; inp = sys.stdin.readline
import heapq

N, E = map(int, inp().split())
graph = [[] for _ in range(N + 1)]

INF = 1000000
# start -> Trough1 -> Trough2 -> end, start -> Trough2 -> Trough1 -> end 중 최소값을 구하면 된다
distStart = [INF for _ in range(N + 1)]
distThrough1 = [INF for _ in range(N + 1)]
distThrough2 = [INF for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, inp().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향

def dijkstra(dist, start):
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        dis, next = heapq.heappop(pq)
        if dis > dist[next]:
            continue

        for nextNode, nextDist in graph[next]:
            if dist[nextNode] > nextDist + dis:
                dist[nextNode] = nextDist + dis
                heapq.heappush(pq, (dist[nextNode], nextNode))


through1, through2 = map(int, inp().split())

dijkstra(distStart, 1) # 3개를 구해서 경우의 수를 따져 최소 경로를 구한다
dijkstra(distThrough1, through1)
dijkstra(distThrough2, through2)

ans = min(distStart[through1] + distThrough1[through2] + distThrough2[N], distStart[through2] + distThrough1[through1] + distThrough2[N])
if ans >= INF:
    print(-1)
else:
    print(ans)