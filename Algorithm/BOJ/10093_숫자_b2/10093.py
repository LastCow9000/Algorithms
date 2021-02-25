# boj 10093 숫자 b2
# https://www.acmicpc.net/problem/10093

a, b = map(int, input().split())
if b > a:  # b가 더 크면 b-a
    print(b - a - 1)  # 두 수의 차이
    for num in range(a + 1, b):
        print(num, end=" ")
elif a > b:  # a가 더 크면 a-b
    print(a - b - 1)
    for num in range(b + 1, a):
        print(num, end=" ")
else:  # 예외 두 수가 같으면 0
    print(a-b)
