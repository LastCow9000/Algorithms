# boj 5347 LCM s4
# noj.am/5347

def gcd(a, b):
    gcd = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = max(gcd, i)
    return gcd

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    lcm = a * b // gcd(a, b)
    print(lcm)