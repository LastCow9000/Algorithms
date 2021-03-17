# boj 1436 영화감독 숌 s5
# noj.am/1436

N = int(input())
cnt = 0
n = 665

while cnt != N:  # count와 찾는 번째 수가 동일하면 stop
    n += 1  # 665부터 1씩 증가시킴. 완탐
    if str(n).find("666") != -1:  # 666이라는 문자열이 있다면 그 인덱스 반환 -> 없을 경우 -1반환
        cnt += 1  # 666이라는 문자열이 있다면 cnt++

print(n)
