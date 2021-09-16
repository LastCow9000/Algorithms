# boj 5912 팰린드롬수 b1
# noj.am/1259

while True:
    data = input()
    if not int(data):
        break
    print('yes') if data == data[::-1] else print('no')