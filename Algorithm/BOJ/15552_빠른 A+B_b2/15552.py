# boj 15552 빠른 A+B b2
# https://www.acmicpc.net/problem/15552

import sys

T = int(input())
for i in range(T):
    input_data = sys.stdin.readline()  # 빠르게 입력받기
    A, B = map(int, input_data.rstrip().split())
    print(A+B)
