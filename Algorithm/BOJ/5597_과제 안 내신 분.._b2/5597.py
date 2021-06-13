# boj 5597 과제 안 내신 분..? b2
# noj.am/5597

_set = {int(input()) for _ in range(28)}
for i in range(1, 31):
    if i not in _set:
        print(i)
