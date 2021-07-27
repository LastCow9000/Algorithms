# boj 9342 염색체 s4
# noj.am/9342

strings = ['A', 'B', 'C', 'D', 'E', 'F']
T = int(input())
for _ in range(T):
    tc = input()
    
    if not tc[0] in strings:
        print('Good')
        continue
    
    if len(tc) != 3 and tc[1] != 'A':
        print('Good')
        continue
    
    idx_F = tc.find('F')
    if idx_F < 0:
        print('Good')
        continue
    else:
        idx_C = tc.find('C')
        if idx_C < 0:
            print('Good')
            continue

        find_idx = -1    
        for i in range(idx_C, len(tc)):
            if tc[i] != 'C':
                find_idx = i
                break
        else:
            print("Infected!")
            continue

        if (find_idx + 1 == len(tc) - 1) and (tc[find_idx + 1] in strings):
            print("Infected!")
            continue
        else:
            print('Good')