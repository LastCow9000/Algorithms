# boj 11866 요세푸스 문제0 s4
# noj.am/11866

from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N + 1)])  # 1~N까지 덱 생성
ans = []

while dq:  # dq가 1이상일때까지
    dq.rotate(-(K - 1))  # 맨 앞 두개를 뒤로 보낸다 => 그러면 맨 앞이 3번째가 됨
    ans.append(str(dq.popleft()))  # 맨 앞 원소를 빼서 결과 리스트에 담는다

print(f'<{", ".join(ans)}>')  # 언팩킹(join)을 위해 윗줄에서 str화
