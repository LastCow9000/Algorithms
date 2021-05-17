# boj 2504 괄호의 값 s2
# noj.am/2504

string = list(input())
_stack = []
ans = []
tmp = 1
prev_c = ""

for c in string:
    if not _stack and (c == ")" or c == "]"):
        print(0)
        break

    # 분배법칙을 이용
    if c == "(" or c == "[":
        _stack.append(c)
        if c == "(":
            prev_c = "("
            tmp *= 2
        else:
            prev_c = "["
            tmp *= 3

    elif c == ")":
        if prev_c == "(":
            ans.append(tmp)
        elif _stack[-1] != "(":
            print(0)
            break
        _stack.pop()
        prev_c = ")"
        tmp //= 2

    else:  # ]
        if prev_c == "[":
            ans.append(tmp)
        elif _stack[-1] != "[":
            print(0)
            break
        _stack.pop()
        prev_c = "]"
        tmp //= 3

else:
    print(sum(ans)) if not _stack else print(0)
