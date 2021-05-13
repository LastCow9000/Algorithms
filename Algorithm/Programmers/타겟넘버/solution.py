# programmers 타겟넘버 lv2
# https://programmers.co.kr/learn/courses/30/lessons/43165

ans = 0


def backtracking(numbs, t, res, cnt):
    global ans
    if cnt == len(numbs):
        if res == t:
            ans += 1
            return
        return

    backtracking(numbs, t, res + numbs[cnt], cnt + 1)
    backtracking(numbs, t, res - numbs[cnt], cnt + 1)


def solution(numbers, target):
    global ans
    backtracking(numbers, target, 0, 0)
    return ans


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    solution(numbers, target)
    print(ans)
