# boj 14889 스타트와 링크(삼성기출) s3
# noj.am/14889

import itertools

# 나의 첫 풀이
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
case = itertools.combinations(range(1, N + 1), N // 2)  # 조합을 이용해 팀 나누기
res = []

for team in case:
    teamS = []
    teamL = []
    sRes = 0
    lRes = 0
    for i in range(1, N + 1):
        if i in team:        # 조합에 있는 원소는 S팀
            teamS.append(i)  # ex) 1 3 5
        else:                # 조합에 없는 원소는 L팀
            teamL.append(i)  # ex) 2 4 6

    teamSScore = itertools.permutations(
        teamS, 2)  # 1 3, 1 5, 3 1, 3 5, 5 1, 5 3    순열로 다시 팀원의 순열을 뽑아냄
    teamLScore = itertools.permutations(
        teamL, 2)  # 2 4, 2 6, 4 2, 4 6, 6 2, 6 4

    for score in teamSScore:  # 팀원 점수의 합
        x, y = score
        sRes += S[x - 1][y - 1]  # 팀원 번호가 1부터 시작하므로 인덱스를 맞추기 위해 -1 씩

    for score in teamLScore:
        x, y = score
        lRes += S[x - 1][y - 1]

    res.append(abs(sRes - lRes))


print(min(res))

'''
# 더 깔끔하게
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
ans = 99999999999


def sol(comb):
    teamS = []
    teamL = []
    _set = set(comb)
    for i in range(1, N + 1):
        if i in _set:
            teamS.append(i)  # 1, 3, 5
        else:
            teamL.append(i)  # 2, 4, 6

    abilityS, abilityL = 0, 0
    for i in range(0, N // 2):  # 1 3, 1 5, 3 5 만 돌게끔
        for j in range(i + 1, N // 2):
            abilityS += S[teamS[i] - 1][teamS[j] - 1] + \
                S[teamS[j] - 1][teamS[i] - 1]
            abilityL += S[teamL[i] - 1][teamL[j] - 1] + \
                S[teamL[j] - 1][teamL[i] - 1]

    return abs(abilityS - abilityL)


for comb in itertools.combinations(range(1, N + 1), N // 2):
    ans = min(ans, sol(comb))

print(ans)
'''
'''
# 조합말고 순열을 이용한 풀이
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
ans = 99999999999

team = []  # 2 팀이므로 0 이면 S팀, 1이면 L팀으로 가정
for i in range(N // 2):
    team.append(0)
for i in range(N // 2):
    team.append(1)


def sol(perm):
    teamS = []
    teamL = []

    for idx, val in enumerate(perm):
        if val == 0:
            teamS.append(idx)
        else:
            teamL.append(idx)

    abilityS, abilityL = 0, 0
    for i in range(0, N // 2):  # 1 3, 1 5, 3 5 만 돌게끔
        for j in range(i + 1, N // 2):
            abilityS += S[teamS[i] - 1][teamS[j] - 1] + \
                S[teamS[j] - 1][teamS[i] - 1]
            abilityL += S[teamL[i] - 1][teamL[j] - 1] + \
                S[teamL[j] - 1][teamL[i] - 1]

    return abs(abilityS - abilityL)


for perm in itertools.permutations(team, N):
    ans = min(ans, sol(perm))

print(ans)
'''
