# boj 1929 소수 구하기 s2
# noj.am/1929

M, N = map(int, input().split())

def find_primes(): # 에라토스테네스의 체
    is_prime = [False, False] + [True] * 1_000_000
    prime_list = []
    for i in range(2, 1_000_001):
        if is_prime[i]:
            prime_list.append(i)
            for j in range(i + i, 1_000_001, i):
                is_prime[j] = False
    
    return prime_list


prime_list = find_primes()
ans = []
for prime in prime_list:
    if prime > N:
        break
    if M <= prime <=N:
        print(prime)
