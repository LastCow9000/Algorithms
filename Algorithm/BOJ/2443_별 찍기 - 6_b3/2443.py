# boj 2443 별 찍기 - 6 b3
# https://www.acmicpc.net/problem/2443
N = int(input())
for i in range(N, 0, -1):  # 별의 갯수가 점점 줄어드므로 거꾸로 돌리기
    for _ in range(N - i):  # N행에 공백 N개 출력
        print(" ", end="")
    for _ in range(2 * i - 1):  # N행에 별 (2n-1)개 출력
        print("*", end="")
    print()  # 행 바꿈
