# Programmers 네트워크 lv3
# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    cnt = 0
    
    for i in range(0, n):
        for j in range(0, n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    # print(graph)
    
    def dfs(start):
        visited[start] = True
        
        for v in graph[start]:
            if not visited[v]:
                dfs(v)
        
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
    
    return cnt


if __name__ == "__main__":
    n1, computers1 = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # 2
    n2, computers2 = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # 1
    print(solution(n1, computers1))
    print(solution(n2, computers2))