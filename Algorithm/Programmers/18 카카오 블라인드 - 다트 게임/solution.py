# 2018 KAKAO BLIND RECRUITME 다트 게임 lv1
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    ans = []
    tmp = 0

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == "1" and dartResult[i + 1] == "0":
                continue
            else:
                if dartResult[i - 1] == "1" and dartResult[i] == "0":
                    tmp = 10
                else:
                    tmp = int(dartResult[i])
        elif dartResult[i] == "S":
            ans.append(tmp)
        elif dartResult[i] == "D":
            tmp = tmp ** 2
            ans.append(tmp)
        elif dartResult[i] == "T":
            tmp = tmp ** 3
            ans.append(tmp)
        elif dartResult[i] == "*":
            if len(ans) <= 1:
                ans[0] = ans[0] * 2
            else:
                lastVal = ans.pop() * 2
                secondLastVal = ans.pop() * 2
                ans.append(secondLastVal)
                ans.append(lastVal)
        elif dartResult[i] == "#":
            lastVal = ans.pop() * -1
            ans.append(lastVal)

    return sum(ans)
