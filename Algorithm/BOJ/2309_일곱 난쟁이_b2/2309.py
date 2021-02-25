# boj 2309 일곱 난쟁이 b2
# https://www.acmicpc.net/problem/2309

height = []
n = 9
while n != 0:
    height.append(int(input()))  # 9개의 키 입력
    n -= 1

for i in height:  # 2중 for문으로 탐색
    for j in height:
        if j == i:  # 같은 값이면 skip
            continue
        if sum(height) - i - j == 100:  # 9개의 키합에서 2개의 값을 뺀게 100이라면
            height.remove(i)  # 키 리스트에서 그 값을삭제
            height.remove(j)

for k in sorted(height):  # 한 줄씩 출력
    print(k)
