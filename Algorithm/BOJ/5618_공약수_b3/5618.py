# boj 5618 공약수 b3
# noj.am/5618
import sys
inp = sys.stdin.readline

n = int(inp())
num = list(map(int, inp().split()))
ans = set()


def gcd(m, n):
    return gcd(n, m % n) if n else m


_gcd = gcd(num[0], gcd(num[-1], num[-2]))

for i in range(1, _gcd + 1):
    if _gcd % i == 0:
        ans.add(i)
        ans.add(int(_gcd / i))
    if i * i == _gcd:
        ans.add(i)
        break
ans = sorted(list(ans))
for dt in ans:
    print(dt)
