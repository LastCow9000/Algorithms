# boj 9012 괄호 s4
# noj.am/9012

for _ in range(int(input())):
    ps = list(input())
    _stack = []  # 아래 코드들이 실행이 끝나고 새로 입력받을때 stack을 비워줌
    for j in range(len(ps)):
        if ps[j] == ")":  # )를 입력받으면 ( pop
            if len(_stack) == 0:  # ( 가 없는데 )가 들어오면 No
                print("NO")
                break
            _stack.pop()
        else:  # ( 면 push
            _stack.append(ps[j])
    else:  # for문이 break가 안났으면 실행
        print("YES") if len(_stack) == 0 else print("NO")
