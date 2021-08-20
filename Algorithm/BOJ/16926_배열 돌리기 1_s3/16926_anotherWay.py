# boj 16926 배열 돌리기 1 s3
# noj.am/16926
import sys; inp = sys.stdin.readline


def rotate(mat, R):
    for _ in range(R):
        top, left = 0, 0
        bottom, right = len(mat) - 1, len(mat[0]) - 1

        # 상 좌 하 우 순으로 회전(스왑)
        while top < bottom and left < right:
            prev = mat[top + 1][right] # 우상단 한칸 아래값부터 회전
            
            for i in range(right, left - 1, -1):
                mat[top][i], prev = prev, mat[top][i]
            top += 1

            for i in range(top, bottom + 1):
                mat[i][left], prev = prev, mat[i][left]
            left += 1

            for i in range(left, right + 1):
                mat[bottom][i], prev = prev, mat[bottom][i]
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                mat[i][right], prev = prev, mat[i][right]
            right -= 1


N, M, R = map(int, inp().split())
_list = [list(map(int, inp().split())) for _ in range(N)]

rotate(_list, R)

for mat in _list:
    print(*mat)
