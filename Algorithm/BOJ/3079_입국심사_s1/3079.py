# boj 3079 입국심사 s1
# noj.am/3079

N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]

time.sort()  # 이분탐색을 위한 정렬


def cntResult(val):  # 시간에 따른 사람수 세는 함수
    res = 0
    for t in time:  # 입력받은 시간 배열을 돌면서
        if t > val:  # 인자값보다 큰 시간값은 종료
            break
        # ex) time = [2, 3, 3, 4, 6, 8]일 때 val=4 라면 4//2 = 2명, 4//3 = 1명, 4//3 = 1명, 4//4 = 1명 -> 4초간 총 5명 심사가능
        res += val // t
    return res


def binarySearch(target):
    left = 1
    right = int(1e19)  # 입력이 M = 1e9, t = 1e9 일때 대비한 값
    ans = 0

    while left <= right:  # 시간을 탐색하면서 목표인원을 달성할 수 있을 경우 시간을 줄일 수 있을까 시도
        mid = (left + right) // 2
        if cntResult(mid) >= target:
            right = mid - 1
            ans = mid
        else:
            left = mid + 1

    return ans


print(binarySearch(M))
