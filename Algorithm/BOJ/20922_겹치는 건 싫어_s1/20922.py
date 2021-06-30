# boj 20922 겹치는 건 싫어 s1
# noj.am/20922
import sys; inp = sys.stdin.readline

N, K = map(int, inp().split())
_list = list(map(int, inp().split()))

left = 0
right = 0
maxLen = 0
countArr = [0] * 100001

while right < N:
    if countArr[_list[right]] == K: # 지금 보는 원소의 갯수가 K개라면 left를 좁혀서 줄여본다
        countArr[_list[left]] -= 1
        left += 1
    else: # 지금 보는 원소의 갯수가 K개 보다 작다면 right를 늘려준다 
        maxLen = max(maxLen, right - left)
        countArr[_list[right]] += 1 # 나온 원수의 갯수를 세준다
        right += 1

print(maxLen + 1)