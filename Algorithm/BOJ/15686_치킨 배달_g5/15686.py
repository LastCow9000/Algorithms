# boj 16686 치킨 배달 g5
# noj.am/15686

# 1 조합으로 치킨집 뽑기
# 2 뽑은 치킨집과의 치킨거리 완탐(최소값 갱신해가며)
# 3 도시 치킨거리 최소값구하기

from itertools import combinations as cb

def parse_map(N, city_map): # 치킨집과 집 위치 구하기
    home_list = []
    ck_list = []
    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1:
                home_list.append((i, j))
            elif city_map[i][j] == 2:
                ck_list.append((i, j))

    return home_list, ck_list


def find_distance(home_list, ck_list, cnt):
    picked_ck = []
    ck_dis_list = []

    # 조합으로 cnt 개수만큼 뽑는 경우의 수 구하기
    for ck in cb(ck_list, cnt):
        picked_ck.append(list(ck))

    # 경우의 수마다 치킨거리 구하기
    for position in picked_ck:

        # N은 50이 최대이므로 50 * 50 = 2500이 최대거리이므로 최소거리를 찾기 위해 초기값 세팅
        ck_dis = {k:3000 for k in range(len(home_list))} 
        
        for x, y in position:
            for idx, (h_x, h_y) in enumerate(home_list):
                dis = abs(h_x - x) + abs(h_y - y)
                
                if ck_dis[idx] > dis: # 최소값 갱신하면서 치킨 거리 구하기
                    ck_dis[idx] = dis

            city_dis = 0
            for k, v in ck_dis.items():
                city_dis += v

            ck_dis_list.append(city_dis) # 경우의 수에 따른 도시 거리를 구해서 추가

    return ck_dis_list

def solution():
    N, M = map(int, input().split())
    city_map = [list(map(int, input().split())) for _ in range(N)]
    home_list, ck_list = parse_map(N, city_map)
    ck_dis = find_distance(home_list, ck_list, M)

    print(min(ck_dis))

if __name__ == "__main__":
    solution()