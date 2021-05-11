# programmers 124 나라의 숫자 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12899#

def solution(n):
    ans_list = [4, 1, 2]
    ans = ""
    while n:  # 나머지를 구해서 앞에서부터 더해준다음 결과를 뒤집음
        b = n % 3
        ans += str(ans_list[b])
        if b == 0:  # 3으로 나누어 떨어지면 몫에서 1을 빼줌
            n = n // 3 - 1
            continue
        n //= 3
    return ans[::-1]
