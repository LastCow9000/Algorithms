# boj 4134 다음 소수 s4
# noj.am/4134

for _ in range(int(input())):
    n = int(input())

    if n <= 1:
        print(2)
        continue

    maxRange = 80000
    flag = [False, False] + [True] * (maxRange - 1)
    
    for num in range(2, maxRange + 1):
        if flag[num]:
            for i in range(num + num, maxRange + 1, num):
                flag[i] = False

    num = n
    while True:
        for i in range(int(num ** 0.5) + 1):
            if flag[i]:
                if num % i == 0:
                    num += 1
                    break
        else:
            print(num)
            break

'''
특정 수의 양의 제곱근 이하의 소수들로 나누어 떨어지면 소수x 
'''