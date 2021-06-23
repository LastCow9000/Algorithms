# programmers 입국심사 lv3
# https://programmers.co.kr/learn/courses/30/lessons/43238
def confirmCount(time, times):
    res = 0
    for t in times:
        res +=  time // t
    return res

def solution(n, times):
    left = 0
    right = max(times) * n
    ans = 0


    while left <= right:
        mid = (left + right) // 2
        if confirmCount(mid, times) >= n:
            ans = mid    
            right = mid - 1
        else:
            left = mid + 1

    return ans

if __name__ == "__main__":
    n1, times1 = 6, [7, 10]
    n2, times2 = 1, [1000]
    n3, times3 = 3, [1, 1, 1]
    n4, times4 = 9, [10, 6, 4, 12, 15, 1, 3, 7, 8]
    n5, times5 = 3, [1, 99, 99]
    n6, times6 = 3, [1, 2, 3]
    print(solution(n1, times1))
    print(solution(n2, times2))
    print(solution(n3, times3))
    print(solution(n4, times4))
    print(solution(n5, times5))
    print(solution(n6, times6))