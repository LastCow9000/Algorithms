# boj 9375 패션왕 신해빈 s3
# noj.am/9375

from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(int)  # 모든 value는 0으로 기본 초기화
    ans = 1

    for i in range(n):
        ck = input().split()  # 옷 이름과 옷 종류 입력
        clothes[ck[1]] += 1  # key는 옷의 종류
    for value in clothes.values():  # 사전의 값들을 돌면서 +1하고 곱해줌
        ans *= (value + 1)
    print(ans-1)  # 아무것도 입지 않는 갯수인 1개 빼서 출력


'''
(headgear입는 경우의수 + 입지 않는 경우의 수(1)) * 
(eyewear 입는 경우의 수 + 입지 않는 경우의 수(1))
- 아예 아무것도 입지 않는 경우의 수(1)

(2 + 1) * (1 + 1) - 1 = 5
'''
