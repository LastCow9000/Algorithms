# 예상 대진표 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    cnt = 1
    while True:
        if abs(a - b) == 1 and ((a < b and b % 2) or (a > b and a % 2)) == 0:
            return cnt

        if a % 2 == 0:
            a = a // 2
        elif a % 2 == 1:
            a = (a + 1) // 2
        if b % 2 == 0:
            b = b // 2
        elif b % 2 == 1:
            b = (b + 1) // 2
        cnt += 1


if __name__ == "__main__":
    N, A, B = 8, 4, 7
    print(solution(N, A, B))
