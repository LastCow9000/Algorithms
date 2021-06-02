# boj 21275 폰 호석만 s3
# noj.am/21275

str1, str2 = input().split()

if str1.isdigit() and str2.isdigit() and str1 == str2:
    print("Multiple")
    exit(0)

num1 = []
num2 = []

for val in str1:
    if val.isdigit():
        num1.append(int(val))
    else:
        num1.append(ord(val) - 87)

for val in str2:
    if val.isdigit():
        num2.append(int(val))
    else:
        num2.append(ord(val) - 87)

num1.reverse()
num2.reverse()

res1 = []
res2 = []

for i in range(37):
    sum = 0
    for idx, num in enumerate(num1):
        if num < i:
            sum += num * (i ** idx)
    res1.append(sum)

for i in range(37):
    sum = 0
    for idx, num in enumerate(num2):
        if num < i:
            sum += num * (i ** idx)
    res2.append(sum)


ans = set(res1) & set(res2)
ans.remove(0)

if len(ans) == 0:
    print("Impossible")
elif len(ans) == 1:
    if (res1.index(*ans) == res2.index(*ans)):
        print("Impossible")
    else:
        print(*ans, res1.index(*ans), res2.index(*ans), sep=" ")
else:
    print("Multiple")

'''
abcde
fghij
klmno
pqrst
uvwxy
z
        473
  448        456
e    p      j    h
14   25     19   17
32          24

주어진수 아스키 이용해서 변환
'''