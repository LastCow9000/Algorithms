# Programmers 다음 큰 숫자 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def isSameOneCnt(num, nCnt):
    s = str(format(num, 'b'))
    numCnt = s.count('1')
    if numCnt == nCnt:
        return True
    return False

def solution(n):
    s = str(format(n, 'b'))
    nCnt = s.count('1')

    num = n
    while True:
        num += 1
        if isSameOneCnt(num, nCnt):
            return num
        