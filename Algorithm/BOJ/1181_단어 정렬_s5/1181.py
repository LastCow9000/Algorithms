# boj 1181 단어 정렬 s5
# noj.am/1181

import sys

N = int(sys.stdin.readline().rstrip())
words = list(set([sys.stdin.readline().rstrip()
                  for _ in range(N)]))  # 입력받은 리스트를 set화해서 중복제거후 다시 list화
words.sort(key=lambda x: (len(x), x))  # 첫 번째 정렬기준은 값의 길이, 두번 째 정렬기준은 값
print(*words, sep='\n')
