# https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())
product = str(A * B * C)
arr = [0] * 10

for i in range(10):
    arr[i] = product.count(str(i))

for result in arr:
    print(result)
