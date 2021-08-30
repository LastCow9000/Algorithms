# boj 4344 평균은 넘겠지 b1
# noj.am/4344

for i in range(int(input())):
    N, *score = map(int, input().split())
    avg = sum(score) / len(score)
    res = [s for s in score if s > avg]
    ans = len(res) / len(score) * 100
    print(f'{ans:.3f}%')