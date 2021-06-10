# 행렬 테두리 회전하기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42747#

def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    for i in range(length + 1):
        cnt = len([citation for citation in citations if citation >= i])
        if cnt >= i:
            answer = max(answer, i)
    return answer