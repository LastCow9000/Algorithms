# 2581 소수 s5
# noj.am/2581

M = int(input())
N = int(input())
prime = []

# 2부터 자기 자신까지 증가시키면서 나누는데 나누어지는 숫자가 2개이상 이면 소수x
for num in range(M, N + 1):
    cnt = 0
    for i in range(2, num + 1): 
        if num % i == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 1:
        prime.append(num)

print(-1) if len(prime) == 0 else print(sum(prime), prime[0], sep="\n")