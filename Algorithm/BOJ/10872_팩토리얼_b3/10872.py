# boj 10872 팩토리얼 b3
# noj.am/10872

def factorial(N):
    if N <= 1:
        return 1
    return N * factorial(N - 1)


N = int(input())
print(factorial(N))
