# 2개 이하로 다른 비트 lv2
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            num = format(num, 'b')
            if '0' in num:
                num = num[::-1]
                idx = num.index('0')
                num = num[:idx - 1] + '01' + num[idx + 1:]
                num = num[::-1]
                answer.append(int(num, 2))
                '''
                10011 -> 1 10 01 뒤집기 전
                10101 -> 1 01 01 뒤집은 후
                '''
            else:
                num = int('10' + str(num)[1:], 2)
                answer.append(num)
    return answer
'''
1: 2
3: 5
5: 6
7: 11
9: 10
11: 13
13: 14

1사이에 0이 존재하면 땡기고
1사이에 0이 존재하지 않으면 맨앞1을 땡긴다
'''


if __name__ == "__main__":
    numbers = [5,7]
    print(solution(numbers))