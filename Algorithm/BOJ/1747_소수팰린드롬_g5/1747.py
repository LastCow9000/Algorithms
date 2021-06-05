# boj 1747 소수&팰린드롬 g5
# noj.am/1747

N = int(input())
if N == 1: 
    print(2)
    exit(0)
maxRange = int(1e6)
flag = [False, False] + [True] * (maxRange - 1)

for num in range(2, maxRange + 1):
    if flag[num]:
        
        for i in range(num + num, maxRange + 1, num):
            flag[i] = False

num = N
while True:
    for i in range(int(num ** 0.5) + 1):
        if (flag[i] and num % i == 0) or str(num) != str(num)[::-1]:
            num += 1
            break

    else:    
        print(num)
        break