# boj 1157 단어 공부 b1
# noj.am/1157

data = list(input().upper())
alpha_cnt = [0] * 26

for dt in data:
    alpha_cnt[ord(dt) - 65] += 1

max_cnt = max(alpha_cnt)
if alpha_cnt.count(max_cnt) > 1:
    print('?')
elif alpha_cnt.count(max_cnt) == 1:
    print(chr(alpha_cnt.index(max_cnt) + 65))