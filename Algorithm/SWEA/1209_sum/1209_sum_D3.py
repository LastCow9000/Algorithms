# 1209. [S/W 문제해결 기본] 2일차 - Sum D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh

for i in range(10):  # 테스트 케이스가 10개
    n = int(input())
    tc = [list(map(int, input().split())) for _ in range(100)]  # 이차원 배열 입력

    max = 0
    x_sum1 = 0  # 우하단방향 대각선합
    x_sum2 = 0  # 좌하단방향 대각선합
    col_sum = 0  # 열 합

    for i in range(100):  # 1행부터 100행까지
        if max < sum(tc[i]):  # 각 행의 합과 최대값 비교
            max = sum(tc[i])

    for i in range(100):  # 우하단방향 대각선합
        x_sum1 += tc[i][i]

    for i in range(99, 0, -1):  # 좌하단방향 대각선합
        x_sum2 += tc[i][i]

    if max < x_sum1:  # 최대값과 대각선합 비교
        max = x_sum1
        if max < x_sum2:
            max = x_sum2

    # 열 합 구하기 ex) arr[0][0] + arr[1][0] + arr[2][0] + ... + arr[99][0]
    for i in range(100):
        col_sum = 0  # 열 합 초기화
        for j in range(100):
            col_sum += tc[j][i]
        if max < col_sum:
            max = col_sum

    print(f'#{n} {max}')
