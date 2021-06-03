# programmers 큰 수 만들기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    _stack = []
    for num in number:
        while _stack and num > _stack[-1] and k != 0:
            _stack.pop()
            k -= 1
        _stack.append(num)

    if k != 0:
        _stack = _stack[:-k]

    return ''.join(_stack)


if __name__ == "__main__":
    number1, k1 = "1924",	2
    number2, k2 = "1231234", 3
    number3, k3 = "4177252841", 4
		
    print(solution(number1, k1))
    print(solution(number2, k2))
    print(solution(number3, k3))