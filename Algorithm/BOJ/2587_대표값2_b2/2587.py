# boj 2587 대표값 b2
# https://www.acmicpc.net/problem/2587

nums = []
for i in range(5):  # 5개 입력받음
    nums.append(int(input()))
print(sum(nums)//len(nums))  # 평균 출력
print(sorted(nums)[2])  # 중앙값 출력
