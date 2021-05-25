# boj 2745 진법 변환 b2
# noj.am/2745

_input = input().split()
N = list(_input[0])
B = int(_input[1])
res = 0
idx = len(N) - 1

for num in N:
    if num.isdigit():
        res += int(num) * (B ** idx)
    else:
        res += (ord(num) - 55) * (B ** idx)
    idx -= 1

print(res)
