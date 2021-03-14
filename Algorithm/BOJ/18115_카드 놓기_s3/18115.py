# boj 18115 카드 놓기 s3
# noj.am/18115
from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))  # 기술
ans = deque()

for i in range(1, N + 1):  # 1 ~ N
    if A[N - i] == 1:  # 마지막 기술부터. 1이라면 맨 앞에 삽입
        ans.appendleft(i)
    elif A[N - i] == 2:  # 2라면 두번째에 삽입
        ans.insert(1, i)
    else:  # 3이라면 맨 뒤에 삽입
        ans.append(i)

print(*ans)


'''
1일때 appnedleft

2일때 a=popleft  appendleft appendleft(a)

3일때 append
'''
