# boj 1966 프린터 큐 s3
# noj.am/1966

from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    priorityAndIdx = deque([[pri, idx] for idx, pri in enumerate(
        map(int, input().split()))])  # 우선순위와 인덱스 2차원 배열  [[pri][idx], [pri][idx], [pri][idx]]
    cnt = 0
    while priorityAndIdx:  # 덱의 길이가 1이상 일때까지 돈다.
        # 우선순위의 최대값과 덱의 첫번째 원소 우선순위가 같다면 dequeue할 대상.
        if max(priorityAndIdx)[0] == priorityAndIdx[0][0]:
            cnt += 1  # dequeue 횟수 증가
            # dequeue할 대상값 중 '알고자 하는 인덱스'와 '덱의 맨 앞 인덱스'가 같을 때 횟수 출력
            if M == priorityAndIdx[0][1]:
                print(cnt)
                break
            else:  # 알고자 하는 인덱스가 아닐 경우 dequeue
                priorityAndIdx.popleft()
        else:  # 맨 앞의 우선순위가 최대가 아니라면 맨 뒤로 보낸다.
            priorityAndIdx.rotate(-1)

'''
li = [[0, 1], [1, 1], [2, 9], [3, 1], [4, 1], [5, 1]]
lit = [[1, 0], [1, 1], [9, 2], [1, 3], [1, 4], [1, 5]]
print(max(li)) # [5, 1]
print(max(lit)) # [9, 2]
'''
