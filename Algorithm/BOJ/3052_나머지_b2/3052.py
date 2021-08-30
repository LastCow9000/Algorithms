# boj 3052 나머지 b2
# noj.am/3052

digits = [int(input()) for _ in range(10)]
mod = [0] * 42
res = set()

for digit in digits:
    mod[digit % 42] += 1

for idx, val in enumerate(mod):
    if val > 0:
        res.add(idx)

print(len(res))