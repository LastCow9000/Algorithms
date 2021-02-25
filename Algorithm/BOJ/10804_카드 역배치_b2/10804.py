# boj 10804 카드 역배치 b2
# https://www.acmicpc.net/problem/10804

cards = [i for i in range(1, 21)]  # 1~20카드

for i in range(10):  # 10개의 구간
    a, b = map(int, input().split())
    if a < b:
        x = cards[a - 1:b]  # 리스트 슬라이스 a-1 번 인덱스부터 b-1까지
        del cards[a - 1:b]  # 기존 리스트에서 슬라이스한 리스트값들 삭제
        x.reverse()  # 슬라이스한 리스트 뒤집음
        for i in x:  # 다시 기존 리스트에 삽입
            cards.insert(a - 1, i)
            a += 1  # 인덱스 하나씩 증가시키면서
    elif a > b:
        x = cards[b - 1:a]
        del cards[b - 1:a]
        x.reverse()
        del x
        for i in x:
            cards.insert(b - 1, i)
            b += 1

for card in cards:
    print(card, end=" ")
