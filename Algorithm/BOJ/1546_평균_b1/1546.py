# boj 1546 평균 b1
# noj.am/1546

N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = []

for num in score:
    new_score.append(num / max_score * 100)

ans = sum(new_score) / N
print(ans)