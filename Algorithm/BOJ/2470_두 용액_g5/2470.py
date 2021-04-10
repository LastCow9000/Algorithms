# boj 2470 두 용액 g5
# noj.am/2470

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

left = 0  # 투포인터 양쪽 끝
right = len(solution) - 1
minVal = int(2e9)

while left != right:  # 양쪽 포인터가 만나면 끝
    tmp = solution[left] + solution[right]
    if abs(tmp) < minVal:  # 두 값을 더한 절대값이 최소값보다 작다면 갱신
        minVal = abs(tmp)
        res = [solution[left], solution[right]]

    if tmp > 0:  # 두 값을 더했는데 0보다 크다면 우측 포인터를 좌측으로 이동시켜 값 축소
        right -= 1
    else:  # 0보다 작다면 좌측 포인터를 우측으로 이동시켜 값 증대
        left += 1

print(*res)
