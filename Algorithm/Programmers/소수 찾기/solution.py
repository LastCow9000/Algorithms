# 소수 찾기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42839

# 내림차순 정렬해서 숫자로 합친후 그범위로 에라토스테네스의 체 돌리기
import itertools as it


def perm(list):
    _set = set()
    for i in range(1, len(list) + 1):
        for num in it.permutations(list, i):  # numbers로 가능한 순열
            n = ""
            for c in map(str, num):  # 튜플을 이어붙여서 숫자로
                n += c
            n = int(n)
            _set.add(n)
    return _set


def solution(numbers):
    num_list = list(numbers)
    num_list.sort(reverse=True)
    num_set = perm(num_list)
    cnt = 0

    n = ""
    for c in map(str, num_list):  # 리스트 원소 이어붙여서 숫자로
        n += c
    n = int(n)

    # 에라토스테네스의 체
    flag = [False, False] + [True] * (n - 1)
    ans = []

    for i in range(2, n + 1):
        if flag[i]:
            ans.append(i)
            for j in range(i * 2, n + 1, i):
                flag[j] = False

    for num in num_set:
        if num in set(ans):
            cnt += 1

    return cnt


if __name__ == "__main__":
    numbers1 = "17"
    numbers2 = "011"
    print(solution(numbers1))
    print(solution(numbers2))
