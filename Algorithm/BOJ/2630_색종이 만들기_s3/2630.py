# boj 2630 색종이 만들기 s3
# noj.am/2630
import sys; r = sys.stdin.readline

# (0,0), (0, N의 반), (N의 반, 0), (N의 반, N의 반)
# 첫 점이 하양(0)인지 파랑(1)인지 판별
# 반복문 돌면서 범위안의 모든 값들이 첫점과 같은지 판단
# 다르면 다시 나눔
def divide_paper(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != color:
                divide_paper(x, y, N // 2) # 2사분면
                divide_paper(x, y + N // 2, N // 2) # 1사분면
                divide_paper(x + N // 2, y, N // 2) # 3사분면
                divide_paper(x + N // 2, y + N // 2, N // 2) # 4사분면
                return

    res[color] += 1


N = int(r())
paper = [list(map(int, r().split())) for _ in range(N)]
res = [0, 0]
divide_paper(0, 0, N)
print(*res, sep='\n')