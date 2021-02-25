# boj 11328 Strfry b2
# https://www.acmicpc.net/problem/11328
import sys

N = int(input())

for i in range(N):
    tc1, tc2 = sys.stdin.readline().rstrip().split()
    if sorted(tc1) == sorted(tc2):
        print("Possible")
    else:
        print("Impossible")
