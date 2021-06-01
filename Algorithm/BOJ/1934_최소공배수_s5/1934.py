# boj 1934 최소공배수 s5
# noj.am/1934

def gcd(a, b):
    gcd = 0
    for i in range(1, max(a, b) + 1): # 둘 중 더 큰 수까지만 돌면 됨
        if a % i == 0 and b % i == 0:
            gcd = max(gcd, i)
    return gcd

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(int(input())):
    print(lcm(*map(int, input().split())))