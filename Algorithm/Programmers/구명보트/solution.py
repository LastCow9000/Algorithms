# 구명보트 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    cnt = 0
    sumWeight = 0
    while i <= j:
        sumWeight = people[i] + people[j]
        if sumWeight <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        cnt += 1

    return cnt


if __name__ == "__main__":
    people1, limit1 = [70, 50, 80, 50], 100  # 3
    people2, limit2 = [70, 80, 50], 100 # 3
    print(solution(people1, limit1))
    print(solution(people2, limit2))