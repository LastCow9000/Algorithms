# boj 10845 큐 s4
# noj.am/10845

import sys; r = sys.stdin.readline

class queue:
    def __init__(self):
        self.list = []

    def push(self, num):
        self.list.append(num)
    
    def pop(self):
        return self.list.pop(0) if self.list else -1 
    
    def size(self):
        return len(self.list)

    def empty(self):
        return 0 if self.list else 1
    
    def front(self):
        return self.list[0] if self.list else -1
    
    def back(self):
        return self.list[-1] if self.list else -1

def solution():
    q = queue()
    N = int(r())

    for _ in range(N):
        cmd = r().rstrip().split()
        if cmd[0] == 'push':
            q.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            print(q.pop())
        elif cmd[0] == 'size':
            print(q.size())
        elif cmd[0] == 'empty':
            print(q.empty())
        elif cmd[0] == 'front':
            print(q.front())
        elif cmd[0] == 'back':
            print(q.back())


if __name__ == '__main__':
    solution()