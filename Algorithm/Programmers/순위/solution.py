# Programmers 순위 lv3
# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for win, lose in results: # 이겼으면 1, 졌으면 -1, 결과를 모르면 0으로 초기화
        graph[win][lose] = 1
        graph[lose][win] = -1

    for k in range(n + 1): # 플로이드 워셜
        for i in range(n + 1):
            for j in range(n + 1):
                # i가 k한테 이기고(지고) k가 j한테 이겼(졌)으면 i는 j한테 이김
                if graph[i][k] == graph[k][j] == 1 and graph[i][j] == 0:
                    graph[i][j] = 1
                elif graph[i][k] == graph[k][j] == -1 and graph[i][j] == 0:
                    graph[i][j] = -1
    
    for i in range(1, n + 1):
        # (자기 자신을 제외하고 모두 승패가 났는지 확인) 0이 한개면 성립
        # 그러나 1번 선수부터 시작하므로 0번행 버리고 0번 선수의 0까지 카운트하여 2개가 맞는지 확인
        if graph[i].count(0) == 2: 
            answer += 1


    return answer


if __name__ == '__main__':
    n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]] # 3
    print(solution(n, results))