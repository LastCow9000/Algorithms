# boj 2805 나무 자르기 s3
# noj.am/2805

# 전형적인 파라메트릭 서치
import sys; r = sys.stdin.readline

def check(height):
    sum_height = 0
    for tree in trees:
        tmp = tree - height
        if tmp > 0:
            sum_height += tmp
        tmp = 0
    
    return sum_height


N, M = map(int, r().split())
trees = list(map(int, r().split()))
left = 0
right = int(2e9)
ans = -1

while left <= right:
    mid = (left + right) // 2
    if check(mid) >= M:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)