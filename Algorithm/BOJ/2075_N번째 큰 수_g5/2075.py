# boj 2075 N번째 큰 수 g5
# noj.am/2075
import sys
import heapq

inp = sys.stdin.readline
N = int(inp())
heap = list(map(int, inp().split()))

for _ in range(N - 1):
    _list = list(map(int, inp().split()))
    for n in _list:
        heapq.heappushpop(heap, n)

print(min(heap))

'''
# 최소 힙(우선순위 큐) 풀이
N 길이의 힙을 만들고 입력받는 값을 계속 push한 후 pop 하여 최소값을 빼낸다
N번째 큰 수라는건 N길이이 힙에서 가장 작은 수이다
ex) 
N = 5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49


12 7 9 15 5인 힙에서 pushpop(13)을 하면 12 7 9 15 13이 되고 pushpop(8) -> 12 9 15 13 8
마지막엔 52 49 48 41 35 가 남고 5번째로 큰수는 35이다
'''
