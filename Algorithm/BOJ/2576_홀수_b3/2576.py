# boj 2576 홀수 b3
# https://www.acmicpc.net/problem/2576

def isOdd(nums):  # 홀수 판별
    oddNum = [num for num in nums if num % 2 == 1]  # 홀수인 것들만 리스트컴프리헨션
    if len(oddNum) == 0:
        return -1  # 홀수가 없을 경우 -1
    sumOdd = sum(oddNum)
    minOdd = min(oddNum)
    return f'{sumOdd}\n{minOdd}'  # 홀수의합과 최솟값 리턴


nums = []  # 자연수 입력받을 리스트

for i in range(7):  # 1~7번째 줄까지 자연수 입력받음
    nums.append(int(input()))
print(isOdd(nums))
