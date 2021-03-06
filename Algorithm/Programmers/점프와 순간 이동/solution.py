# programmers 점프와 순간 이동 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    while n > 1:
        if n % 2 == 1:
            ans += 1
        n //= 2
    return ans + 1

'''
625 312...1  156 78 39 19...1  9...1  4...1   2   1 
5000 = 625 * 2 * 2 * 2
6 = 3  1...1
5 = 2...1  1

1: 1
2: 1
3: 2
4: 1
5: 2
6: 2
7: 3
8: 1
9: 2
10: 2

2의 n승은 1

2 4 8 16 32 64 128 256 512 1024 2048 4096 8192
3 6 12 24 48 96 192 384 768 1536 3072 6144
5 10 20 40 80 160 320 640 1280 2560 5120
'''