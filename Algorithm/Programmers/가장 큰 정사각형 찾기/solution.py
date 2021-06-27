# 가장 큰 정사각형 찾기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12905

import itertools

def solution(board):
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                
    board = itertools.chain(*board) # 2차원 리스트 모든 원소를 풀어서 1차원 리스트로 변형
    res = max(board) ** 2
    
    return res


if __name__ == "__main__":
    board1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]  # 9
    board2 = [[0,0,1,1],[1,1,1,1]]  # 4
    print(solution(board1))
    print(solution(board2))

'''
a b
c d        d를 볼때 왼(c), 위(b) ,왼위(a) 중 최소값 + 1이 길이
'''