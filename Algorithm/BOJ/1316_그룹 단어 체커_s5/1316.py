# boj 1316 그룹 단어 체커 s5
# noj.am/1316

N = int(input())
words = [input() for _ in range(N)]

cnt = 0

for word in words:
    
    _set = set()
    prev = ''

    for c in word:
        if c != prev and c in _set: # 현재 문자가 이전 문자와 다른데 이미 나왔었던 문자라면 그룹단어가 아니다
            break
        prev = c
        _set.add(c)
    else: # for문이 break가 걸리지 않고 끝나면 수행
        cnt += 1

print(cnt)