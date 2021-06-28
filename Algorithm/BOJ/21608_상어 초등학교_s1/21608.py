# boj 21608 상어 초등학교 s1
# noj.am/21608

N = int(input())
pos = [[-1] * N for _ in range(N)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

for _ in range(N ** 2):
    student, *likes = map(int, input().split())
    maxPosCnt = 0
    maxLikeCnt = 0
    r, c = 0, 0

    for i in range(N):
        for j in range(N):
            if pos[i][j] == -1:
                posCnt = 0
                likeCnt = 0

                for k in range(4):
                    X, Y = i + dx[k], j + dy[k]
                    if 0 <= X < N and 0 <= Y < N:
                        if pos[X][Y] == -1: 
                            posCnt += 1
                        if pos[X][Y] in likes:
                            likeCnt += 1

                if likeCnt > maxLikeCnt:
                    maxLikeCnt = likeCnt
                    maxPosCnt = posCnt
                    r, c = i, j
                elif likeCnt == maxLikeCnt and posCnt > maxPosCnt:
                    maxPosCnt = posCnt
                    r, c = i, j

    pos[r][c] = student

print(pos)


