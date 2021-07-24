# boj 6550 부분 문자열 s5
# noj.am/6550

while True:
    try:
        s, t = input().split()

        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    print("Yes")
                    break

        else:
            print("No")
    except EOFError:
        break

