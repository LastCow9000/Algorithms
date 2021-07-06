# 피보나치 수 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12945

def fibo(n): # bottom-up
    dp = [0, 1] + [-1] * 99999
    for i in range(2, 100001):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

def solution(n):
    answer = fibo(n)
    return answer %  1234567

print(solution(10))
