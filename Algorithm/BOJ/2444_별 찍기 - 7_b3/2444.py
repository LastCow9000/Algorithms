# 2444 별 찍기 - 7 b3
# https://www.acmicpc.net/problem/2444

N = int(input())

for i in range(N):  # 0행부터 N - 1행까지
    for _ in range(N - i, 1, -1):  # 공백의 갯수가 N-i개부터 행이 바뀔 때 마다 1개씩 증가
        print(" ", end="")
    for _ in range(2 * i + 1):  # 별의 갯수가 (2*행+1)개
        print("*", end="")
    print()

# 반으로 나눠서 구현

for i in range(N - 1, 0, -1):  # N-1개의 행까지
    for _ in range(N - i):  # 공백의 갯수가 행이 바뀔 때 마다 1개씩증가(i가 점점 1씩 작아지므로)
        print(" ", end="")
    for _ in range(2 * i - 1):  # 별의 갯수 홀수개(2*행-1)로 감소
        print("*", end="")
    print()
