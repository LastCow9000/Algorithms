# boj 1212 8진수 2진수 b3
# noj.am/1212

def numToBinary(num):
    res = ''
    while num >= 1:
        if num == 1:
            res += str(num)
            break
        res += str(num % 2)
        num //= 2

    return '%03d' % (int(res[::-1]))

# print(numToBinary(1))
# print(numToBinary(2))
# print(numToBinary(3))
# print(numToBinary(4))
# print(numToBinary(5))
# print(numToBinary(6))
# print(numToBinary(7))

n = input()
numbers = list(n)
ans = ''
for num in numbers:
    if num == '0':
        ans += '000'
        continue
    ans += numToBinary(int(num))
print(int(ans))