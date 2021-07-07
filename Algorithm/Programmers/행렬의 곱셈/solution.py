# 행렬의 곱셈 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    ans = []
    for row in arr1:
        ansRow = []
        for col in zip(*arr2): # 열끼리 한 튜플로 묶어줌
            ansRow.append(sum([x * y for x, y in zip(row, col)])) # sum(각 인덱스의 원소끼리 튜플로 묶어서 서로 곱해줌)
        ans.append(ansRow)

    return ans