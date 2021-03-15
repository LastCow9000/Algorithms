# boj 2776 암기왕 s3
# noj.am/2776

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    setNote1 = set(note1)
    setNote2 = set(note2)
    Intersection = setNote1 & setNote2  # 교집합 공통된 수만 뽑기

    for i in note2:  # note2 리스트를 돌면서 교집합 안에 해당 원소가 있으면 1
        print(1) if i in Intersection else print(0)
