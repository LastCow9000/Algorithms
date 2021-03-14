# boj 1874 스택 수열 s3
# noj.am/1874

n = int(input())
_stack = []
res = []  # 결과값
cnt = 0
flag = "YES"  # NO일경우 NO출력
for _ in range(n):
    _input = int(input())
    while cnt < _input:  # 입력받은 값보다 작은값들(1부터) stack에 push
        cnt += 1
        _stack.append(cnt)
        res.append("+")
    if _stack[-1] == _input:  # 입력받은 값보다 크거나 같을 때부터 판단. 스택의 마지막값이
        _stack.pop()         # 입력받은 값과 같다면 pop
        res.append("-")
    else:  # 스택의 마지막 값이 입력값과 같은 상황이 나오지 않는 경우 NO
        flag = "NO"

print('\n'.join(res)) if flag == "YES" else print("NO")
