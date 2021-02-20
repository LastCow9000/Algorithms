# boj 2562 최댓값 b2
# https://www.acmicpc.net/problem/2562

nums = []  # 입력받을 리스트

for i in range(9):  # 첫째 줄부터 아홉 번째 줄까지 입력받음
    nums.append(int(input()))

maxValue = max(nums)  # 입력받은값중에서 최댓값
print(maxValue)
print(nums.index(maxValue)+1)  # 최댓값이 몇 번째 수인지 출력
