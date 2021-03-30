# boj 13908 비밀번호 g5
# noj.am/13908

n, m = map(int, input().split())
knownPass = list(map(int, input().split()))


def recursive(res):
    if len(res) == n:  # 원하는 길이인데 비밀번호에 알고 있는 값이 없다면 찾는 게 아니므로 0 반환
        for pw in knownPass:
            if pw not in res:
                return 0
        return 1

    cnt = 0
    for i in range(10):
        res.append(i)
        cnt += recursive(res)
        res.pop()

    return cnt


print(recursive([]))
