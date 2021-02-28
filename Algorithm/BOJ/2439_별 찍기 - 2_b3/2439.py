# boj 2439 별 찍기 - 2 b3
# https://www.acmicpc.net/problem/2439

N = int(input())
for i in range(N):  # N행
    for _ in range(N - i, 1, -1):  # 0행은 공백4개.. 1행은 공백3개.. N행은 공백 (N-행)개
        print(" ", end="")
    for _ in range(i + 1):  # N행은 '*' N개
        print("*", end="")
    print()  # 행 바꿈
