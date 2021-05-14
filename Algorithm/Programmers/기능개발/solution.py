# Programmers 기능개발 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math
from collections import deque


def solution(progresses, speeds):
    dq = deque()
    _stack = []
    ans = []
    cnt = 1  # 처음엔 무조건 1일 이상이 걸리므로
    tmpCnt = 0
    for i in range(len(progresses)):
        # 각각 걸리는 날 deque에 추가
        dq.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while dq:  # duque가 빌 때까지
        _stack.append(dq.popleft())

        for i in range(len(dq)):
            # stack의 마지막 값보다 덱의 원소들이 작다면 임시 카운트++
            if len(dq) != 0 and dq[i] <= _stack[-1]:
                tmpCnt += 1
            else:
                break

        while tmpCnt != 0:  # 임시 카운트만큼 덱에서 뺴서 스택에 넣어주고 카운트를 증가시켜줌
            tmpCnt -= 1
            _stack.append(dq.popleft())
            cnt += 1
        ans.append(cnt)
        cnt = 1  # cnt 초기화

    return ans


if __name__ == "__main__":
    progresses1, speeds1 = [93, 30, 55], [1, 30, 5]
    progresses2, speeds2 = [95, 90, 99, 99, 80, 99], [
        1, 1, 1, 1, 1, 1]  # 5 10 1 1 20 1
    progresses3, speeds3 = [85, 88, 87], [1, 1, 1]
    progresses4, speeds4 = [99, 99, 99], [1, 1, 1]
    print(solution(progresses1, speeds1))
    print(solution(progresses2, speeds2))
    print(solution(progresses3, speeds3))
    print(solution(progresses4, speeds4))
