# 2018 KAKAO BLIND RECRUITMENT 비밀지도 lv1
# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
from collections import deque


def solution(n, arr1, arr2):
    answer = []
    tempArr = []
    for i in range(n):
        tempArr.append(arr1[i] | arr2[i])
    for arr in tempArr:
        ans = ""
        results = format(arr, 'b')
        dq = deque(results)
        if len(dq) != n:
            for i in range(n - len(dq)):
                dq.appendleft("0")
        for res in dq:
            if res == "1":
                ans += "#"
            else:
                ans += " "
        answer.append(ans)

    return answer


if __name__ == "__main__":
    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    print(solution(n, arr1, arr2))
