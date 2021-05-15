# boj 1935 후위 표기식2 s3
# noj.am/1935

N = int(input())
postfix = list(input())
val = [int(input()) for _ in range(N)]
_stack = []
ans = []

for expression in postfix:
    if expression.isalpha():  # 알파벳이면 val의 인덱스 번호에 해당하는 값을 추가
        _stack.append(val[ord(expression) - 65])  # A의 아스키코드 값 = 65
        continue
    if expression == "+":
        _stack.append(_stack.pop() + _stack.pop())
    elif expression == "-":  # - 와 / 는 값의 순서가 중요하기 때문에 변수에 지정
        b, f = _stack.pop(), _stack.pop()
        _stack.append(f - b)
    elif expression == "*":
        _stack.append(_stack.pop() * _stack.pop())
    elif expression == "/":
        b, f = _stack.pop(), _stack.pop()
        _stack.append(f / b)

print("%.2f" % (round(_stack.pop(), 2)))  # 소수 둘째자리까지 반올림하여 표시
