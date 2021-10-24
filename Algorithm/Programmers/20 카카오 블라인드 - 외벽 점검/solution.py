# Programmers 2020 KAKAO BLIND RECRUITMENT - 외벽 점검 Lv3
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations as pm

# 원 둘레를 탐색해야 하기 때문에 길이만큼 각 원소에 더하여 배열을 확장
# weak의 길이 만큼의 구간을 잘라서 확인한다 
# ex) 취약점이 4개면 [1, 5, 6, 10, 13 ,17, 18, 25] 에서 1~10, 5~13, 6~17 

# 초기에 구간의 첫 값(작은 값)을 지정하고 친구들이 탐색할 수 있는 
# 거리를 더해서 구간의 최종값보다 크거나 같은지 확인

# 크거나 같다면 (ex [5, 6, 10, 13]의 구간에서 5에다가 친구가 탐색할 수 있는 
# 거리인 4,3,2 를 더하면 14이므로 13보다 크다) 취약지점 탐색을 끝낸 것임

# 순열을 이용하여 [1, 2, 3, 4], [3, 4, 1, 2], [4, 2, 1, 3] 등의 모든 경우의 수를 완탐해서
# 최소값의 답을 찾는다

def solution(n, weak, dist):
    ans = int(1e9)
    l = len(weak)
    circle_weak = weak + [w + n for w in weak]
    # print(circle_weak)  # [1, 5, 6, 10, 13 ,17, 18, 25]
    
    for i in range(l):
        for case in pm(dist):
            see_window = circle_weak[i:i + l]
            start_point = circle_weak[i]
            cnt = 1
            for d in case:
                start_point += d
                if start_point >= circle_weak[i + l - 1]:
                    ans = min(ans, cnt)
                    break
                cnt += 1
                start_point = min(list(filter(lambda x:x > start_point, see_window))) # 시작값을 변경하는데 구간에서 이전 값보다 크면서 최소인 값
                
    return ans if ans != int(1e9) else -1


if __name__ == '__main__':
    n1, weak1, dist1 = 12, [1, 5, 6, 10], [1, 2, 3, 4] # 2
    n2, weak2, dist2 = 12, [1, 3, 4, 9, 10], [3, 5, 7] # 1
    print(solution(n1, weak1, dist1))
    # print(solution(n2, weak2, dist2))