# boj 1085 직사각형에서 탈출 b3
# noj.am/1085

x, y, w, h = map(int, input().split())
print(min(abs(x - w), abs(y - h), x, y))