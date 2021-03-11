# boj 2164 카드2 s4
# noj.am/2164
from collections import deque

N = int(input())
card = deque(i for i in range(1, N+1))  # 덱으로 카드 설정

while len(card) > 1:  # 1장 남을때까지
    card.popleft()  # 맨 앞 deque
    card.rotate(-1)  # 맨 앞 카드를 맨뒤로 이동

print(card[0])  # deque의 첫번째 원소
