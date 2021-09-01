# boj 4673 셀프 넘버 s5
# noj.am/4673

nums = set([i for i in range(1, 10001)])
d_list = []
i = 0

while True:
    i += 1
    tmp = i + sum(map(int, list(str(i))))
    if i <= 10000: 
        d_list.append(tmp)
        continue
    break

res = nums - set(d_list)
for r in sorted(list(res)):
    print(r)