# boj 2217 로프 s4
# noj.am/2217

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()
res = 0

for i in range(N):
    res = max(res, rope[i] * (N - i))

print(res)

'''
총 개수에서 해당하는 인덱스의 번호를 뺀수를 해당 값에 곱하면
그 값으로 만들 수 있는 중량이 나온다.
ex) N = 6, rope = [0, 12, 48, 150, 450, 2000] 일때
0, 60, 192, 450, 900, 2000의 무게를 들 수 있다. 
'''