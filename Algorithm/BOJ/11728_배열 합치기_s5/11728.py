# boj 배열 합치기 s5
# noj.am/11728
# import sys; inp = sys.stdin.readline

# N, M = map(int, inp().split())
# A = list(map(int, inp().split()))
# B = list(map(int, inp().split()))

# A.extend(B)
# A.sort()
# print(*A)


import sys; inp = sys.stdin.readline

N, M = map(int, inp().split())
A = list(map(int, inp().split()))
B = list(map(int, inp().split()))

i = 0
j = 0
res = []

while i != N and j != M:
    if A[i] < B[j]:
        res.append(A[i])
        i += 1
    else:
        res.append(B[j])
        j += 1

if i == N:
    while j != M:
        res.append(B[j])
        j += 1
        
else:
    while i != N:
        res.append(A[i])
        i += 1

print(*res)

