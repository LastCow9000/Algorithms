# boj 2442 별 찍기 - 5 b3
# https://www.acmicpc.net/problem/2442

N = int(input())
for i in range(N):  # N행
    for _ in range(N - i, 1, -1):  # 공백 (N-행) 개 출력
        print(" ", end="")
    for _ in range(2 * i + 1):  # 홀수(2*행+1)개의 별 출력
        print("*", end="")
    print()  # 행 바꿈
