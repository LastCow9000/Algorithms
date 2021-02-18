# boj 10871 x보다 작은 수 b2
# https://www.acmicpc.net/problem/10871

N, X = map(int, (input().split()))
A = list(map(int, input().split()))  # 수열A

for a in A:  # A의 원소를 하나씩 확인하면서
    if X > a:  # X보다 값이 작으면 출력하고(개행문자말고 스페이스바까지)
        print(a, end=" ")
