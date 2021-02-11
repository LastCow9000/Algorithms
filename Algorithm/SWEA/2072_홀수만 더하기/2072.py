# 2072. 홀수만 더하기
'''
import sys

t = int(input())
oddNumber = []
total = 0
for j in range(t):
    case = list(map(int, sys.stdin.readline().split()))
    for i in range(10):
        if case[i] % 2 == 1:
            total += case[i]
    oddNumber.append(total)
    total = 0
for i in range(1, t + 1):
    print('#{0} {1}'.format(i, oddNumber[i - 1]))
'''

t = int(input())
for j in range(1, t + 1):
    case = sum([int(i) for i in input().split(' ') if int(i) % 2 == 1])
    print('#{0} {1}'.format(j, case))
    case = []
