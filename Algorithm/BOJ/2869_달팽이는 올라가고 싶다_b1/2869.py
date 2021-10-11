import math

A, B, V = map(int, input().split())
ans = (V - B) / (A - B) # 마지막 날에 미끄러지지 않는 거리를 미리 빼놓음

print(math.ceil(ans))