# boj 2438 별 찍기 - 1 b3
# https://www.acmicpc.net/problem/2438

N = int(input())
for i in range(1, N+1):  # N번쨰 줄까지
    for j in range(1, i+1):  # 1행에는 1개, 2행에는 2개, 3행에는 3개...
        print("*", end="")
    print()  # 한줄 출력후 줄바꿈
