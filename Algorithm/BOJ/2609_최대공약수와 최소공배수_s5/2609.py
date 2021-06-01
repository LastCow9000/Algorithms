# boj 최대공약수와 최소공배수 s5
# noj.am/2609

def gcd(a, b):
    gcd = 0
    for i in range(1, 10001):
        if a % i == 0 and b % i == 0:
            gcd = max(gcd, i)
    return gcd

def lcm(a, b, gcd): # 두 수의 곱 / 최대공약수 = 최소공배수
    return a * b // gcd


a, b = map(int, input().split())
gcd = gcd(a, b)
print(gcd)
lcm = lcm(a, b, gcd)
print(lcm)