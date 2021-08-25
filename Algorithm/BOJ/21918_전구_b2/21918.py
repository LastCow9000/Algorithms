# boj 21918 전구 b2
# noj.am/21918

N, M = map(int, input().split())
bulb = list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulb[b - 1] = c
    elif a == 2:
        for i in range(b, c + 1):
            if bulb[i - 1]:
                bulb[i - 1] = 0
            else:
                bulb[i - 1] = 1
    elif a == 3:
        for i in range(b, c + 1):
            bulb[i - 1] = 0
    elif a == 4:
        for i in range(b, c + 1):
            bulb[i - 1] = 1

print(*bulb)