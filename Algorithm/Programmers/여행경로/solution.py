# Programmers여행경로 lv3
# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict

ans = []

def dfs(s, graph, n):
    ans.append(s)

    if len(ans) == n + 1: # 결과에 티켓 수보다 1개만큼 더 쌓이면 답
        return

    for e in graph[s]:
        graph[s].remove(e)

        dfs(e, graph, n)
    
        if len(ans) != n + 1: # 탐색 중 이어지는 경로가 없는데 아직 답이 아닌 경우 롤백
            graph[s].insert(0, e)
            ans.pop()
            continue

def solution(tickets):
    graph = defaultdict(list)
    
    for s, e in tickets: # graph 만들기
        graph[s].append(e)

    for k in graph.keys(): # 알파뱃 순서가 앞서는 경로를 찾으므로 정렬
        graph[k].sort()

    n = len(tickets)
    dfs('ICN', graph, n)
    
    return ans


if __name__ == '__main__':
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] # ["ICN", "JFK", "HND", "IAD"]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    tickets3 = [["ICN", "B"], ["ICN", "D"], ["D", "E"], ["E", "ICN"]] # ["ICN", "D", "E", "ICN", "B"]
    tickets4 = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]] # ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]
    # print(solution(tickets1))
    # print(solution(tickets2))
    # print(solution(tickets3))
    print(solution(tickets4))