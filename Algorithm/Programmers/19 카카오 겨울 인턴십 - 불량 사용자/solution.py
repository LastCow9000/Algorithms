# 2019 카카오 개발자 겨울 인턴십 - 불량 사용자 lv3
# https://programmers.co.kr/learn/courses/30/lessons/64064

''' 먼저 밴 리스트에서 제거된 것에서 일치하는게 있을 때를 체크하지 못함 
    [a, b, c]    ban = [*, *, a] 일 때..

    # 빼지말고 다 검사해서 하나라도 일치하는게 있으면 ans++ 해보자
'''
from itertools import permutations as pm

# 길이체크 and 한글자씩 보면서 맞는지 체크 * 이면 패스
def isValid(case, banned_id):
    for i in range(len(case)):
        if len(case[i]) != len(banned_id[i]):
            return False

        for j in range(len(case[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != case[i][j]:
                return False

    return True

def solution(user_id, banned_id):
    # 길이만큼 순열 돌려서 리스트 만들고
    cases = pm(user_id, len(banned_id))    # [[a, b, c], [b, c, a]......[c, b, a]]
    ban_res = []

    for case in cases:
        if isValid(case, banned_id):
            users = set(case)  # {a, b, c}
            if users not in ban_res:
                ban_res.append(users)

    return len(ban_res)

if __name__ == "__main__":
    user_id1, banned_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"] # 2
    user_id2, banned_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"] # 2
    user_id3, banned_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"] # 3
    print(solution(user_id1, banned_id1))
    print(solution(user_id2, banned_id2))
    print(solution(user_id3, banned_id3))




'''
# 혼자 푼 것

먼저 밴 리스트에서 제거된 것에서 일치하는게 있을 때를 체크하지 못함
from collections import deque
from itertools import combinations as cb
import copy

def isCorrect(ban_id, user_id):
    for i in range(len(user_id)):
        if ban_id[i] == '*':
            continue
        if ban_id[i] != user_id[i]:
            return False

    return True

def solution(user_id, banned_id):
    answer = 0
    # 길이만큼 콤비네이션 뽑아서 리스트 만들고
    dq = deque(sorted(list(cb(user_id, len(banned_id)))))
    
    # 길이체크 and 한글자씩 보면서 맞는지 체크 * 이면 패스
    while dq:
        banned_id_list : list = copy.deepcopy(banned_id)
        case = dq.popleft() # (frodo, crodo, abc123)
        flag = True

        cnt = 0
        for id in sorted(case): # frodo
            for ban_id in banned_id_list: # "*rodo", "*rodo", "******"
                if len(ban_id) == len(id):
                    if not isCorrect(ban_id, id):
                        flag = False
                    else:
                        flag = True
                        banned_id_list.remove(ban_id)
                        cnt += 1

        if flag and cnt == len(case):
            answer += 1

    return answer


'''