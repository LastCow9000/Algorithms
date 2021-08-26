# boj 1789 수들의 합 s5
# noj.am/1789

def binarySearch(S):
    left = 1
    right = S
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 <= S:
            ans = mid
            left += 1
        else:
            right = mid - 1

    return ans

S = int(input())
print(binarySearch(S))
# 수학공식에 의해 1부터 N까지 더해지는 수를 찾는데
# 이분 탐색 결과 찾는 값과 가장 근접한 숫자가 찾아진다
# 정답이 찾아지면 베스트, 정답이 아니여도 그보다 
# 1 뺀거에서 새로운 자연수를 더하면 정답이 된다
# ex) 200 => 1~19까지 합이 190, 190에서 200이 되려면 10이 필요한대 이미 더한 숫자이므로
# 1~18까지의 합인 171 에서 29를 더하면 된다(1~18: 18개, 29: 1개 => 19개)