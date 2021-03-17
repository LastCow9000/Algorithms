# boj 1620 나는야 포켓몬 마스터 이다솜 s4
# noj.am/1620

from sys import stdin

_input = stdin.readline
N, M = map(int, _input().rstrip().split())
dogamList = [_input().rstrip()
             for _ in range(N)]  # 이름을 부르면 인덱스+1을  출력하기 위한 리스트
# 번호를 부르면 value를 출력하기 위한 사전
dogamDict = {idx + 1: name for idx, name in enumerate(dogamList)}

for _ in range(M):
    question = _input().rstrip()
    if question.isdigit():  # 입력값이 숫자면 사전에서 키값으로 value(포켓몬이름) 찾아옴
        print(dogamDict[int(question)])
    else:  # 입력값이 문자면 리스트에서 몇번 인덱스에 있는지 찾아서 + 1
        print(dogamList.index(question) + 1)
