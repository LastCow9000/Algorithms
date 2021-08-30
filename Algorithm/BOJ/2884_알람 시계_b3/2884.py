# boj 2884 알람 시계 b3
# noj.am/2884

H, M = map(int, input().split())
tmp = H * 60 + M - 45
h, m = tmp // 60, tmp % 60
if h < 0:
    h += 24
print(f'{h} {m}')