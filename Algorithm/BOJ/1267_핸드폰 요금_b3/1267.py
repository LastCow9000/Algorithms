# boj 1267 핸드폰 요금 b3
# https://www.acmicpc.net/submit/1267/26649825

def bill(sec):
    Y = 0
    M = 0
    for i in sec:
        Y += i // 30 * 10 + 10  # 영식 요금제일 경우 합
        M += i // 60 * 15 + 15  # 민식 요금제일 경우 합
    if Y > M:  # 민식이 더 싸다면
        return f'M {M}'
    elif Y < M:
        return f'Y {Y}'
    else:   # 같다면
        return f'Y M {Y}'


n = int(input())
sec = list(map(int, input().split()))
print(bill(sec))
