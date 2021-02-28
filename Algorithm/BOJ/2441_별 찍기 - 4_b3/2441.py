# boj 2441 별 찍기 - 4 b3
# https://www.acmicpc.net/problem/2441
N = int(input())
for i in range(N):  # N행
    for _ in range(i):  # 0행에는 공백0개.. 1행에는 공백1개.. 2행에는 공백2개..
        print(" ", end="")
    for _ in range(N + 1 - i, 1, -1):  # 0행에는 * N개.. 1행에는 N-1개..
        print("*", end="")
    print()  # 행 바꿈
