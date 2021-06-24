# programmers 올바른 괄호 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    _stack = []
    for c in s:
        if _stack and c == ')' and _stack[-1] == '(':
            _stack.pop()
            continue
        _stack.append(c)
    
    return False if _stack else True
        

if __name__ == "__main__":
    s1 = "()()"
    s2 = "(())()"
    s3 = ")()("
    s4 = "(()("
    print(solution(s1))
    print(solution(s2))
    print(solution(s3))
    print(solution(s4))