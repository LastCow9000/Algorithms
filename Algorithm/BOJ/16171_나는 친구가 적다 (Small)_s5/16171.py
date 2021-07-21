# boj 16171 나는 친구가 적다 (Small) s5
# noj.am/16171

S = list(input())
K = input()

string = [c for c in S if not c.isdigit()]

findChar = ''
for i in range(len(string)):

    findChar = ''

    for j in range(i, len(string)):
        findChar += string[j] # 앞에서부터 하나씩 더해가다가
        if len(findChar) == len(K): # 찾는 문자열의 길이가 같아지면 찾는 문자열과 같은지 비교
            if findChar == K:
                print(1)
                exit()

else: # 다 탐색해도 찾는 문자열이 없으면
    print(0)


