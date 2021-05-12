# boj 10828 스택 s4
# noj.am/10828

from collections import deque
import sys

inp = sys.stdin.readline
dq = deque()
for _ in range(int(inp())):
    command = inp().rstrip().split()

    if command[0] == "push_front":
        dq.appendleft(command[1])
    elif command[0] == "push_back":
        dq.append(command[1])
    elif command[0] == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if dq:
            print(dq.pop())
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
