# boj 2751 수 정렬하기 2
# noj.am/2751

import sys; r = sys.stdin.readline
print(*sorted([int(r()) for i in range(int(r()))]), sep='\n')
