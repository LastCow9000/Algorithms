# boj 10870 피보나치 수 5 b2
# noj.am/10870

def pibonachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return pibonachi(n - 1) + pibonachi(n - 2)


n = int(input())
print(pibonachi(n))
