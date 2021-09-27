# 빈 칸의 갯수를 센다음 맨 앞부터 빈칸의 갯수만큼 빈칸을 채우고
# 데이터를 넣는 방식으로 떨어짐을 구현
# def fall(m, n, board): 
#     new_board = [[' '] * n for _ in range(m)]
#     for j in range(n):
#         empty_cnt = 0
#         data = []
#         for i in range(m):
#             if board[i][j] == ' ':
#                 empty_cnt += 1
#             else:
#                 data.append(board[i][j])
        
#         for k in range(empty_cnt, m):
#             new_board[k][j] = data[k - empty_cnt]
    
#     return new_board


def fall(m, n, board): # 파이썬만의 방법
    rotate = list(zip(*board)) # 열과 행 교체
    empty_cnt = [row.count(' ') for row in rotate] # 각 행의 빈 칸 갯수
    data_board = [[i for i in row if i != ' '] for row in rotate] # 각 행의 빈칸이 아닌 데이터 배열
    tmp_board = [[' '] * empty_cnt[i] + data_board[i] for i in range(len(rotate))] # 합치기
    completed_board = [list(col) for col in zip(*tmp_board)] # 재회전
    return completed_board
                
    
def remove(m, n, board):
    # 원래 배열을 건들면 못지우는 경우가 생겨서 쌓아놓고 한 번에 지움
    tmp_remove_board = [[0] * n for _ in range(m)]
    cnt = 0
    for i in range(m - 1): # 끝 범위를 보면 초과되는 범위가 생김
        for j in range(n - 1):
            # 동, 남, 동남쪽이 같다면
            if board[i][j] != ' ' and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                tmp_remove_board[i][j] = 1
                tmp_remove_board[i + 1][j] = 1
                tmp_remove_board[i][j + 1] = 1
                tmp_remove_board[i + 1][j + 1] = 1
                    
    for i in range(m):
        for j in range(n):
            if tmp_remove_board[i][j]:
                board[i][j] = ' '
                cnt += 1
    
    return cnt


def solution(m, n, board):
    new_board = [list(dt) for dt in board] # string배열을 char 배열로
    ans = 0
    
    while True: 
        removed_cnt = remove(m, n, new_board)
        new_board = fall(m, n, new_board)
        ans += removed_cnt
        if removed_cnt == 0: # 지워지는 개수가 0이면 겜 끝
            break
            
    return ans


if __name__ == '__main__':
    m1, n1, board1 = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"] # 14
    m2, n2, board2 = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] # 15
    print(solution(m1, n1, board1))
    print(solution(m2, n2, board2))