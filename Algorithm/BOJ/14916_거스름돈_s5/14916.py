# boj 14916 거스름돈 s5
# noj.am/14916

n = int(input())
cnt = 0
flag = True

while n != 0:  # 2원씩 빼다가 5원으로 나누어 떨어질 수 있을 때 나눠준다
    if n == 1:  # 1원이 남을 경우 거슬러 줄 수 없다
        flag = False
    if n % 5 == 0:
        cnt += n // 5
        break
    n -= 2
    cnt += 1

print(cnt) if flag else print(-1)
