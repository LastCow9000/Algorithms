# boj 2440 별 찍기 - 3 b3
# https://www.acmicpc.net/problem/2440

N = int(input())
for i in range(N):
    for j in range(N + 1 - i, 1, -1):  # 1행 N개, 2행 N-1개, 행이 내려갈수록 커지는 값을 이용해서 빼줘야함
        print("*", end="")
    print()  # 행 바꿈
