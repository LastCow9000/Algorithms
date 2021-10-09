# boj 15829 Hashing b2
# noj.am/15829

L = int(input())
data = list(input())
hashing = list(map(lambda x:(ord(x) - 96), data))
hashed = 0
for i, v in enumerate(hashing):
    hashed += 31 ** i * v
print(hashed % 1234567891)
