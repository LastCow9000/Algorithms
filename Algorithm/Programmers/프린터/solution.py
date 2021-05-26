# 프린터 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    cnt = 0
    idx = 0
    dq = deque([[pri, idx] for idx, pri in enumerate(priorities)])

    while dq:
        if max(dq)[0] == dq[0][0]:
            cnt += 1
            _print = dq.popleft()
            if _print[1] == location:
                return cnt
            continue
        dq.rotate(-1)


if __name__ == "__main__":
    priorities1, location1 = [2, 1, 3, 2], 2
    priorities2, location2 = [1, 1, 9, 1, 1, 1], 0
    print(solution(priorities1, location1))
    print(solution(priorities2, location2))
