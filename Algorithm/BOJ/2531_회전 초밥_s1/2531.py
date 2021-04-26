# boj 2531 회전 초밥 s1
# noj.am/2531
import sys
from collections import defaultdict

# 슬라이딩 윈도우
inp = sys.stdin.readline
N, d, k, c = map(int, inp().split())
sushi = [int(inp()) for _ in range(N)]
sushi.extend(sushi)  # 원형이기 때문에 한번 더 붙임
# sushi += sushi
kinds = defaultdict(int)
kinds[c] += 1  # 쿠폰으로 받은 것 부터 처리

left = 0
right = 0

while right - left != k:  # 초기 k개의 초밥 종류 갯수 입력
    kinds[sushi[right]] += 1
    right += 1

ans = len(kinds)

while right != len(sushi):  # 오른쪽 포인터가 배열범위 밖으로 나가면 stop
    ans = max(ans, len(kinds))
    kinds[sushi[left]] -= 1
    if kinds[sushi[left]] == 0:  # 초밥 종류의 value 값이 0 이면 키 값 삭제
        del kinds[sushi[left]]
    kinds[sushi[right]] += 1
    left += 1  # 슬라이딩 윈도우 이동
    right += 1

print(ans)
