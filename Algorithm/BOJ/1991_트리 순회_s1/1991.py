# boj 1991 트리 순회 s1
# noj.am/1991

N = int(input())
tree = [[0] * 2 for _ in range(N + 1)] # 0: left_child, 1: right_child

def pre_order(node):
    if node:
        print(chr(node + 65), end='')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


def in_order(node):
    if node:
        pre_order(tree[node][0])
        print(chr(node + 65), end='')
        pre_order(tree[node][1])


def post_order(node):
    if node:
        pre_order(tree[node][0])
        pre_order(tree[node][1])
        print(chr(node + 65), end='')

for _ in range(N):
    p, lc, rc = map(lambda x:ord(x) - 65, input().split())
    
    if lc != -19:
        tree[p][0] = lc
    
    if rc != -19:
        tree[p][1] = rc
    
pre_order(1)
print()
in_order(1)
print()
post_order(1)

