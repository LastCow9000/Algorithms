# Programmers 숫자의 표현 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12924

cnt = 0 # 전역변수
ans = 0
def recursive(i, n):
    global cnt
    global ans
    cnt += i
    
    if cnt == n: # 원하는 수가 나왔을 시 결과 ++
        ans += 1
        return
    
    if cnt > n: # 원하는 수 초과시 stop
        return
    
    recursive(i + 1, n) # 1씩 증가시키면서 더해줌
    
def solution(n):
    global ans
    global cnt
    
    for i in range(1, n + 1):
        cnt = 0
        recursive(i, n)
    
    return ans


if __name__ == "__main__":
    print(solution(15))