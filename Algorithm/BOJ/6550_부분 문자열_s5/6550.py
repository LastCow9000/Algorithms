# boj 6550 부분 문자열 s5
# noj.am/6550

while True:
    inp = input()
    if not inp:
        break
    s, t = inp.split()

    i = 0

    for c in t:
        if s[i] == c:
            i += 1
            if i == len(s):
                print("Yes")
                break
            
    print("No")


