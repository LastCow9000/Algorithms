# boj 1312 소수 s5
# noj.am/1312

A, B, N = map(int, input().split())

mod = A % B

while N - 1:
    N -= 1
    mod = (mod * 10) % B

print(mod * 10 // B)