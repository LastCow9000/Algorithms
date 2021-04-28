# boj 5671 호텔 방 번호 s4
# noj.am/5671

N, M = map(int, input().split())
cnt = 0
flag = True

for num in range(N, M + 1):
    length = len(str(num))
    for i in range(length):
        if str(num)[0] == str(num)[i]:
            flag = False
            break
    if flag:
        cnt += 1

    flag = True
print(cnt)
