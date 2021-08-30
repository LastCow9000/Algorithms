# boj 20665 독서실 거리두기 g5
# noj.am/20665
import sys; inp = sys.stdin.readline

N, T, P = map(int, inp().split())

map = [[0] * 101 for _ in range(721)] # 12시간 * 60분
people = [inp().rstrip().split() for _ in range(T)]
people.sort()

def get_minutes(time):
    return int(time[0:2]) * 60 + int(time[2:]) - 540 # 9시가 시작이니 60 * 9 를 빼줌


def get_pos(start):
    max_distance = 0
    pos = 1

    for i in range(1, N + 1):
        if map[start][i] == 1:
            continue

        tmp = 1000
        for j in range(1, N + 1):
            if map[start][j] == 1:
                tmp = min(tmp, abs(i - j)) # 1번에 가까운 낮은 자리

        if max_distance < tmp: # 거리가 가장 먼 곳
            max_distance = tmp
            pos = i
    
    return pos


def sit(start, end, pos):
    for idx in range(start, end):
        map[idx][pos] = 1


def solution():
    for start, end in people:
        start, end = get_minutes(start), get_minutes(end)
        pos = get_pos(start)
        sit(start, end, pos)

    answer = 0
    for i in range(720): # 720분을 다 돌면서 P번 자리가 비어있는 시간 찾기
        if map[i][P] != 1:
            answer += 1
        
    return answer


if __name__ == "__main__":
    print(solution())

