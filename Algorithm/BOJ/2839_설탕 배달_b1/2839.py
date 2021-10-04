# boj 2839 설탕 배달 b1
# noj.am/2839

N = int(input())
ans = 0
while N > 0:
    if N % 5 == 0:
        ans += N // 5
        break
    if N < 3:
        ans = -1
        break
    N -= 3
    ans += 1

print(ans)