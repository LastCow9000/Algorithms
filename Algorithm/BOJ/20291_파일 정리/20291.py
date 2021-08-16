# boj 20291 파일 정리 s4
# noj.am/20291

import re
from collections import defaultdict

N = int(input())
ans = []
_dict = defaultdict(int)
for _ in range(N):
    p = re.compile('\w+\.(\w+)')
    finded_str = p.search(input()).group(1) # regex 그룹화해서 마침표 뒤 뽑기
    # finded_str = input().split('.')[1]
    
    _dict[finded_str] += 1
    ans.append(finded_str)

ans = [*set(ans)] # 키 값 중복 제거
ans.sort()

for k in ans:
    print(f'{k} {_dict[k]}')