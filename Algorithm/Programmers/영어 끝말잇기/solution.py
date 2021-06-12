# 영어 끝말잇기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12981

import math

def solution(n, words):
    ans = ''
    prev = words[0][-1]
    history = set()
    history.add(words[0])
    for i in range(1, len(words)):
        if prev != words[i][0] or words[i] in history:
            ans = [n if (i + 1) % n == 0 else (i + 1) % n,math.ceil((i + 1) / n)]
            break
        prev = words[i][-1]
        history.add(words[i])
    else:
        return [0,0]
    return ans

# ceil(5 / 2) = 3     ceil(9 / 3) = 3
# 5 % 2 = 1        9 % 3 = 0