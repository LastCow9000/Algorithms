# boj 11022 A+B - 8 b3
# noj.am/11022

for i in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')