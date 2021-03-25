# boj 1920 수 찾기 s4
# noj.am/1920
import sys

inp = sys.stdin.readline
N = int(inp().rstrip())
N_list = list(map(int, inp().rstrip().split()))
N_list.sort()  # 이분탐색을 위한 정렬


def binarySerch(target):
    left = 0
    right = len(N_list) - 1

    while left < right:
        mid = (left + right) // 2
        if N_list[mid] < target:  # 찾는 값이 현재 설정된 중간값보다 클 경우 left 옮김
            left = mid + 1
        else:
            right = mid
    return 1 if N_list[left] == target else 0  # 찾는 값이 있을 경우 1


M = int(inp().rstrip())
M_list = list(map(int, inp().rstrip().split()))

for i in M_list:
    print(binarySerch(i))
