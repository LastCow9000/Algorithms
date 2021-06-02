# boj 11653 소인수분해 s4
# noj.am/11653

def findPrime(n):
    flag = [False, False] + [True] * (n - 1)
    prime = []

    for num in range(n + 1):
        if flag[num]:
            prime.append(num)
            for i in range(num, n + 1, num):
                flag[i] = False
    
    return prime

N = int(input())
if N == 1: exit(0)
res = []
prime = findPrime(N)
i = 0

# 소수를 divisor로 사용
while True:
    if N % prime[i] == 0:
        res.append(prime[i])
        N //= prime[i]
        i = 0
        if N == 1:
            break
    else:
        i += 1
        
print(*res, sep="\n")