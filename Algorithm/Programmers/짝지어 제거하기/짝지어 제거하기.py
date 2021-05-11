# programmers 짝지어 제거하기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    _stack = []
    for char in s:
        if _stack and _stack[-1] == char:
            _stack.pop()
            continue
        _stack.append(char)
    return 1 if not _stack else 0
