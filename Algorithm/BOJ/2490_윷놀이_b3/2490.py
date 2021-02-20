# boj 2490 윷놀이
# https://www.acmicpc.net/problem/2490

def resultOFYut(yut):
    result = "E"  # 도, 개, 걸, 윷이 아니면 모(초기값)
    if yut.count(0) == 1:  # 0이 1개면 도
        result = "A"
    elif yut.count(0) == 2:
        result = "B"
    elif yut.count(0) == 3:
        result = "C"
    elif yut.count(0) == 4:  # 0이 4개면 윷
        result = "D"
    return result


for i in range(3):
    yut = list(map(int, input().split()))  # 셋째줄까지 입력받음
    print(resultOFYut(yut))  # 판단
