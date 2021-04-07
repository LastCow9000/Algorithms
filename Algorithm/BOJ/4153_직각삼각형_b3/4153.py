# boj 4153 직각삼각형 b3
# noj.am/4153

while True:
    lines = list(map(int, input().split()))
    if sum(lines) == 0:
        break

    lines.sort()
    if lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2:
        print("right")
    else:
        print("wrong")
