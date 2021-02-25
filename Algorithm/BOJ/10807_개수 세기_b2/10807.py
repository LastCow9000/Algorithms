# boj 10807 개수 세기 b2
# https://www.acmicpc.net/problem/10807

n = int(input())
arr = [int(x) for x in (input().split())]  # 배열 입력
v = int(input())
res = [0] * 201  # 해당하는 인덱스의 갯수를 저장할 배열 선언 및 초기화
for x in arr:  # arr에 있는 원소들을 하나씩 돌면서
    if x < 0:  # 음수일 경우 200을 더해서 101~200번 인덱스에 저장
        res[x + 201] += 1
    else:
        res[x] += 1  # 결과 배열의 해당 인덱스에 갯수를 한개씩 증가
if v < 0:
    print(res[v + 201])
else:
    print(res[v])


# 내장함수 이용해서 간단하게 풀기
''' 
n = int(input())
arr = [int(x) for x in (input().split())]  # 배열 입력
v = int(input())
print(arr.count(v))
'''
