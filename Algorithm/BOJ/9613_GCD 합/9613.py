# boj 9613 GCD 합 s3
# noj.am/9613
from itertools import combinations as cb

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(int(input())):
    n, *nums = map(int, input().split())
    sum = 0
    for a, b in cb(nums, 2):
        sum += gcd(a, b)
    print(sum)