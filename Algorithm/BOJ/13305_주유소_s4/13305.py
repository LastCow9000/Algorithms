# boj 13305 주유소 s4
# noj.am/13305

N = int(input())
distance  = list(map(int, input().split()))
price = list(map(int, input().split()))
ans = 0

currentPrice = price[0]
for i in range(1, N):
    ans += currentPrice * distance[i - 1] # 무조건 현재 위치에서 다음 거리 만큼만 넣는다
    if currentPrice > price[i]: # 현재 가격이 다음 주유소 가격보다 비싸면 현재가격을 다음주유소 가격으로 초기화
        currentPrice = price[i] # 현재 가격이 더 싸다면 계속 현재가격으로 밀어 부친다

print(ans)