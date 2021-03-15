# boj 2346 풍선 터뜨리기 s3
# noj.am/2346

from collections import deque

N = int(input())
_next = deque([[idx+1, __next]  # [풍선번호 = 인덱스+1, 다음이동값 = 입력값] 2차원 배열
               for idx, __next in enumerate(map(int, input().split()))])
res = []

while _next:  # _next deque이 비면 stop
    start = _next.popleft()  # 첫 번째 원소 dequeue
    res.append(start[0])  # 첫번째 원소의 0번 인덱스 = 풍선번호
    nextCount = start[1]  # 첫번째 원소의 1번 인덱스 = 다음 이동값
    if nextCount > 0:  # 다음 이동값이 양수면 1감소된 만큼의 값으로 반시계방향 회전
        _next.rotate(-(nextCount - 1))
    else:  # 음수면 그 값 그대로 시계 방향회전
        _next.rotate(-nextCount)

print(*res)


'''
dq
2차원 enumerate or 배열두개
[[1, 3], [2, 2], [3, 1], [4, -3], [5, -1]]
1   2   3   4   5
3   2   1  -3  -1

'''
