# 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임 lv1
# https://programmers.co.kr/learn/courses/30/lessons/64061
from collections import deque


def solution(board, moves):
    cnt = 0
    _stack = []
    rotate = [deque(list(arr)) for arr in zip(*board)]

    for move in moves:
        dq = rotate[move - 1]
        if not dq:
            continue
        select = dq.popleft()
        while select == 0:
            select = dq.popleft()

        if _stack and _stack[-1] == select:
            _stack.pop()
            cnt += 2
        else:
            _stack.append(select)

        # rotate[move - 1] = list(dq) ########## 생각해보자

    return cnt


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
        0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))
