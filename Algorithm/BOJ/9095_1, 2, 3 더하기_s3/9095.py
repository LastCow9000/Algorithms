# boj 9095 1, 2, 3 더하기 s3
# noj.am/9095

# 재귀로 풀기

T = int(input())


def recursive(N):
    if N < 0:
        return 0
    if N == 0:
        return 1
    return recursive(N - 1) + recursive(N - 2) + recursive(N - 3)


for i in range(T):
    print(recursive(int(input())))
'''
3
{rec 2} + [rec 1] + (rec 0)
{rec 2} + [rec 1] + (1)
{rec 2} + [rec 0] + (1)
{rec 2} +   [1]   + (1)
{rec 1 + rec 0} + [1] + (1)
{rec 1 +   1}   + [1] + (1)
{  1   +   1}   + [1] + (1)


4
rec 3 + rec 2 + rec 1
[rec 3] + 1 + 1 +  1
[rec 2 + rec 1 + rec 0] + 1 + 1 + 1
             4          + 1 + 1 + 1
'''
