# boj 17144 미세먼지 안녕! g4
# noj.am/17144

# 공기청정기의 위치를 찾고
# 미세먼지 확산/ dx, dy/ 범위초과와 공기청정기 위치 확인
# 공기청정기 위는 반시계 방향 회전, 아래는 시계 방향 회전/ 스왑

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

def find_air(): # 청정기 윗부분 위치 반환
    for i in range(R):
        if graph[i][0] == -1:
            return i


def find_dust(): # 먼지가 있는 곳 위치 리스트 반환
    pos = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                pos.append((i, j))
    return pos


def diffuse(air_pos, dust_pos_list):
    # 임시 지도를 만들어서 한번에 원본과 합침
    tmp_air = [[0] * C for _ in range(R)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x, y in dust_pos_list:
        cnt = 0
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < R and 0 <= Y < C and not(Y == 0 and air_pos <= X <= air_pos + 1):
                tmp_air[X][Y] += graph[x][y] // 5
                cnt += 1 # 퍼진 갯수를 세줌

        tmp_air[x][y] += graph[x][y] - cnt * (graph[x][y] // 5)

    tmp_air[air_pos][0] = -1 # 공기청정기 위치 세팅
    tmp_air[air_pos + 1][0] = -1

    return tmp_air


def air_rotate(air_pos):
    # 윗부분 공기 회전
    prev = 0
    for i in range(1, C):
        graph[air_pos][i], prev = prev, graph[air_pos][i]
    for i in range(air_pos - 1, -1, -1):
        graph[i][C - 1], prev = prev, graph[i][C - 1]
    for i in range(C - 2, -1, -1):
        graph[0][i], prev = prev, graph[0][i]
    for i in range(1, air_pos):
        graph[i][0], prev = prev, graph[i][0]

    # 아랫부분 공기 회전
    prev = 0
    air_pos += 1 # 기존 위치는 공기청정기 윗부분이므로
    for i in range(1, C):
        graph[air_pos][i], prev = prev, graph[air_pos][i]
    for i in range(air_pos + 1, R):
        graph[i][C - 1], prev = prev, graph[i][C - 1]
    for i in range(C - 2, -1, -1):
        graph[R - 1][i], prev = prev, graph[R - 1][i]
    for i in range(R - 2, air_pos, -1):
        graph[i][0], prev = prev, graph[i][0]


def solution():
    global graph
    air_pos = find_air()
    for _ in range(T):
        dust_pos_list = find_dust()
        graph = diffuse(air_pos, dust_pos_list)
        air_rotate(air_pos)

    ans = 0
    for row in graph:
        ans += sum(row)
    
    return ans + 2


if __name__ =='__main__':
    print(solution())
