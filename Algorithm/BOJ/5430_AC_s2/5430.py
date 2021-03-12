# boj 5430 AC s2
# noj.am/5430
from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    # [공백없는 쉼표]로 입력받아서 []를 제거하고 쉼표를 공백으로 바꾸고 공백기준으로 split하여 deque 생성
    x = deque(sys.stdin.readline().rstrip().strip(
        '[]').replace(',', ' ').split())

    flag = 0  # 안뒤집어 졌으면0 뒤집어졌으면 1
    for lang in p:
        if lang == 'D':  # 삭제라면
            if len(x) == 0:  # 덱에 입력값이 없다면
                print("error")
                break
            x.popleft() if flag == 0 else x.pop()  # 안뒤집혔으면 deque  뒤집혔으면 맨 뒤값 pop
        else:
            flag = 1 - flag  # R이라면 뒤집는다
    else:  # break 하지 않고 for문이 끝나면 실행
        print('[' + ','.join(x) + ']') if flag == 0 else print('[' +
                                                               ','.join(list(x)[::-1]) + ']')  # unpacking해서 공백없이 쉼표로 구분하여 출력
