# boj 1475 방 번호 s5
# https://www.acmicpc.net/problem/1475

n = list(map(int, input()))  # 9999라면 [9,9,9,9]로 받기
countArray = [0] * 10  # 0~9번 인덱스 초기값 0

for c in n:  # 받을 배열의 각 숫자를 돌면서
    countArray[c] += 1  # 각 숫자의 인덱스에 해당하는 배열값+1
if countArray[6] > countArray[9]:  # 6의 개수가 9의 개수보다 크면
    # 두 수 차이의 반보다 +1만큼 돌면서 ex. 4 1 이면 2번만
    for i in range((countArray[6] - countArray[9]) // 2 + 1):
        if countArray[6] > 1 and countArray[6] != countArray[9]:  # 두 수의 개수가 같아지게하거나
            # 반복문이 끝날 때까지 각 개수를 하나씩 빼고 더해준다.
            countArray[6] -= 1
            countArray[9] += 1
else:
    for i in range((countArray[9] - countArray[6]) // 2 + 1):
        if countArray[9] > 1 and countArray[6] != countArray[9]:
            countArray[9] -= 1
            countArray[6] += 1
if n[0] == 0:  # 예외, 입력이 0일 경우 1 출력
    print(1)
else:
    print(max(countArray))  # 배열중에서 제일 큰 수 뽑기


'''
n = input()

a = []

for i in range(10):
    a.append(n.count(str(i)))

if a[6] == max(a) or a[9] == max(a):
    k = a[6]+a[9]
    if k % 2 == 0:
        a.append(k//2)
    else:
        a.append(k//2+1)
    a[6] = 0
    a[9] = 0

print(max(a))
'''
