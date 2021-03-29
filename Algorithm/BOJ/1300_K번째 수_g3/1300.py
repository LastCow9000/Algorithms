# boj 1300 K번째 수 g3
# noj.am/1300

N = int(input())
K = int(input())


def cntNum(target):  # target이 몇 번째 수인지 판단하는 함수
    res = 0
    for i in range(1, N + 1):
        # 각 행에 존재하는 원소 갯수와 target을 각 행의 값으로 나눈 것중에서 작은 값의 합으로 위치를 판단 (각 행은 그 행 값의 배수로 이루어져있으므로)
        res += min(N, target // i)
    return res


def binarySearch(K):
    left = 1
    right = int(1e9)

    while left < right:  # 범위나 최대값이 아니라 정확한 수를 찾는 이분탐색
        mid = (left + right) // 2
        if cntNum(mid) >= K:  # 판단결과 K번째 수거나 더 크다면 절반이후의 우측에는 값이 존재하지 않으므로
            right = mid
        else:  # mid 값보다 K가 크다면 절반이하 좌측엔 값이 존재하지 않으므로
            left = mid + 1
    return (left + right) // 2


print(binarySearch(K))
