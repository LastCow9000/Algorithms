# boj 1065 한수 s4
# noj.am/1065

N = int(input())
cnt = 0

for i in range(1, N + 1):
    if len(str(i)) <= 2:
        cnt += 1
        continue
    num = list(map(int, str(i)))
    prev = []
    for j in range(len(num) - 1):
        prev.append(num[j + 1] - num[j])
    
    if len(set(prev)) == 1:
        cnt += 1

print(cnt)