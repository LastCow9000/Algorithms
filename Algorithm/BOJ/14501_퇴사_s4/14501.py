# boj 14501 퇴사 s4
# noj.am/14501

N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]


def recursive(day, remain, money):
    if day == N:  # 퇴사날이 되면
        if remain > 0:  # 퇴사날인데 남은 날이 존재한다면 0원
            return 0
        return money

    # 상담안 할 경우
    res = recursive(day + 1, remain - 1, money)  # 날짜는 하루가 더 가고 남은 날짜는 -1

    # 상담할 경우
    if remain <= 0:  # 상담의 남은 기간이 0이하여야 상담가능
        # 상담을 하는 경우와 안하는 경우에서 최대값을 고름
        res = max(res, recursive(day + 1, TP[day][0] - 1, TP[day][1] + money))
    return res


print(recursive(0, 0, 0))
