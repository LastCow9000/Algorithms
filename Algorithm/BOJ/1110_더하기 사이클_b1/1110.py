# boj 1110 더하기 사이클 b1
# noj.am/1110

N = input()
num = N
sum_num = 0
cnt = 0

while True:
    cnt += 1
    if int(num) < 10:
        num = "0" + str(num)
        
    sum_num = num[-1] + str(int(num[0]) + int(num[1]))[-1]
    
    if int(sum_num) == int(N):
        print(cnt)
        break

    # 십의 자리에 0이 있을 경우 제거해주기 위해
    num = str(int(sum_num))
