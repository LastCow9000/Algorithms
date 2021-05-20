# 모의고사 lv1
# https://programmers.co.kr/learn/courses/30/lessons/42840

def scoring(supo, answers, num):
    res = 0
    for i in range(len(answers)):
        j = i % len(supo)
        if answers[i] == supo[j]:
            res += 1
    return res


def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    res = [0] * 4
    ans = []

    res[1] = scoring(supo1, answers, 1)
    res[2] = scoring(supo2, answers, 2)
    res[3] = scoring(supo3, answers, 3)

    return sorted([idx for idx, val in enumerate(res) if max(res) == val])


if __name__ == "__main__":
    answers1 = [1, 2, 3, 4, 5]
    answers2 = [1, 3, 2, 4, 2]
    print(solution(answers1))
    print(solution(answers2))
