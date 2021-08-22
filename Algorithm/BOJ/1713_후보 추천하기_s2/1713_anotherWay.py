# boj 1713 후보 추천하기 s2
# noj.am/1713

N = int(input())
M = int(input())
query = list(map(int, input().split()))
_dict = {}

for idx, num in enumerate(query):
    if len(_dict) >= N and num not in _dict:
        tmp = sorted(_dict.items(), key= lambda x : (x[1][0], x[1][1])) # 추천받은 횟수, 들어온 순서 오름차순 정렬
        del _dict[tmp[0][0]]
    _dict.setdefault(num, [0, idx])[0] += 1 # 기존에 num키를 가진 사전이 있으면 값 반환, 없으면 값의 첫번째 원소(추천cnt) + 1 

print(*sorted(_dict))