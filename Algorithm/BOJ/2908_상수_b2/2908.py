# boj 2908 상수 b2
# noj.am/2908

A, B = map(lambda x : int(x[::-1]), input().split())
print(A) if A > B else print(B)