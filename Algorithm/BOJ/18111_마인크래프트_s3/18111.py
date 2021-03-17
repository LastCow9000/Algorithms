# boj 18111 마인크래프트 s3
# noj.am/18111

# cpp에선 통과하는 완전탐색 풀이지만 파이썬 보정이 없어서 시간초과남

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
minTime = int(1e9)
height = 0

for h in range(257):  # 0~256 높이 완전 탐색
    inven = B
    time = 0

    for i in range(N):
        for j in range(M):
            if land[i][j] < h:  # h높이에 맞출건데 h 높이보다 낮다면 블록쌓기
                time += (h - land[i][j])
                inven -= (h - land[i][j])  # 쌓으므로 인벤의 블록 소모

            elif land[i][j] > h:  # h 높이보다 높다면 블록 깍기
                time += 2 * (land[i][j] - h)
                inven += (land[i][j] - h)  # 깍으므로 인벤에 블록이 쌓임

    if inven < 0:  # 인벤에 있는 블록의 갯수가 음수라면 위의 행동들 없던 일로..
        continue

    if minTime > time:
        minTime = time
        height = h

print(f"{minTime} {height}")

'''
높이까지반복문 완탐
2차원배열로받고
돌면서
높이보다 높으면 깍고
높이보다 낮으면 쌓고
인벤블록이 부족하면 cont
'''
