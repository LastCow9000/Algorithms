# Programmers 2020 KAKAO BLIND RECRUITMENT - 자물쇠와 열쇠 Lv3
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 백트래킹
# lock을 가운데에 두고 key를 모두 넣어볼 수 있는 큰 판을 만들고 다 시도

def rotate(key):
    return list(zip(*key[::-1]))


def check(lock, board):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if board[20 + i][20 + j] == 0:
                return False
    
    return True


def fill(key, board, x, y):
    for i in range(len(key)):
        for j in range(len(key)):
            board[x + i][y + j] ^= key[i][j] # XOR


def move_lock_to_board(lock, board):
    for i in range(len(lock)):
        for j in range(len(lock)):
            board[20 + i][20 + j] = lock[i][j]


def solution(key, lock):
    new_board = [[0] * 60 for _ in range(60)]
    move_lock_to_board(lock, new_board)

    for _ in range(4): # 4번 회전 시도
        for i in range(40):
            for j in range(40):
                fill(key, new_board, i, j)
                if check(lock, new_board):
                    return True
                fill(key, new_board, i, j) # 백트래킹을 위한 원상 복구

        key = rotate(key)
    
    return False


if __name__ == '__main__':
    key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]] # True
    print(solution(key, lock))