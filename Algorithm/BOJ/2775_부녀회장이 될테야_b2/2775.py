# boj 2775 부녀회장이 될테야 b2
# noj.am/2775

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    ans = 0
    floor = [i for i in range(1, n + 1)] # 0층 1 2 3 4
    for i in range(k):
        for j in range(1, n): # 1호는 1로 고정이므로 제외
            floor[j] += floor[j - 1]

    print(floor[n - 1])

'''
1  6  21  56
1  5  15  35
1  4  10  20
1  3  6   10
1  2  3   4
'''