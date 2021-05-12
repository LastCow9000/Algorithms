# boj 1158 요세푸스 문제 s5
# noj.am/1158

from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N + 1)])
cnt = 1
ans = []

while dq:
    if cnt % K == 0:
        ans.append(dq.popleft())
    else:
        dq.append(dq.popleft())
    cnt += 1

print("".join(str(ans)).replace("[", "<").replace("]", ">"))
