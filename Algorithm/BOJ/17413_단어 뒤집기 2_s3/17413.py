# boj 17413 단어 뒤집기 2 s3
# noj.am/17413
import sys

inp = sys.stdin.readline
S = inp()
flag = False
ans = []
res = ""
tmp = ""
stack = []

for c in S:  # 문자를 하나씩 돌면서
    if c == "<":
        if len(tmp) > 0:  # 임시배열에 값이 있으면 결과에 더해줌
            res += tmp
            tmp = ""
        if len(stack) > 0:  # 뒤집기위한 스택에 값이 있으면 결과에 더해줌
            while stack:
                tmp += stack.pop()
            res += tmp
            tmp = ""
        flag = True  # > 나올때까지 뒤집지 않기
        tmp += c  # 그대로 임시배열에 문자를 더해줌

    elif flag:  # <가 나오고 >가 안나온 상태
        if c == ">":
            flag = False
        tmp += c

    elif not flag:  # < > 안이 아니라면
        if len(tmp) > 0:
            res += tmp
            tmp = ""
        if c == " " or c == S[-1]:  # 공백이거나 마지막 값이면 결과값에 뒤집은 값 더해줌
            while stack:
                tmp += stack.pop()
            res += tmp + " "
            tmp = ""
        else:  # 뒤집기위해 스택에 저장
            stack.append(c)

ans.append(res)
print(*ans, sep="")
