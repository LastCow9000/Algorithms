# boj 10808 알파벳 개수 b2
# https://www.acmicpc.net/problem/10808

a_count = [0] * 26  # 알파벳은 26개니까 0으로 26개 초기화
s = input()

for x in s:  # 문자열을 돌면서
    a_count[ord(x)-97] += 1  # a=0번 인덱스, z=26번 인덱스로 설정하고 해당하는 배열에 1씩 더해줌

for i in range(26):
    print(a_count[i], end=" ")
