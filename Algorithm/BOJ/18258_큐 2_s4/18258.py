# boj 18258 큐 2 s4
# noj.am/18258

from collections import deque
import sys

inp = sys.stdin.readline
dq = deque()
for _ in range(int(inp())):
    command = inp().rstrip().split()

    if command[0] == "push":
        dq.append(command[1])
    elif command[0] == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
