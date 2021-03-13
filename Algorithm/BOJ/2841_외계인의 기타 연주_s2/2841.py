# boj 2841 외계인의 기타 연주 s2
# noj.am/2841

N, Prat = map(int, input().split())
_stack = [[0] for _ in range(7)]  # 기타줄 1~6번(0번 무시)
ans = 0

for i in range(N):
    jul, p = map(int, input().split())  # 줄, 프랫
    while _stack[jul][-1] > p:  # 해당 줄번호의 끝값(프랫)이 누르려는 플랫보다 높을 경우 뗀다.
        _stack[jul].pop()
        ans += 1
    # 해당 줄번호의 끝값(프랫)이 누르려는 플랫보다 낮을경우 누른다. (같은 경우는 이미 누르고 있으므로 횟수x)
    if _stack[jul][-1] != p:
        _stack[jul].append(p)
        ans += 1

print(ans)
