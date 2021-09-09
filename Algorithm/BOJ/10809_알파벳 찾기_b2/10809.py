# boj 10809 알파벳 찾기 b2
# noj.am/10809
import string

S = input()
alpha = string.ascii_lowercase
ans = []

for c in alpha:
    if c in S:
        ans.append(S.index(c))
    else:
        ans.append(-1)

print(*ans)