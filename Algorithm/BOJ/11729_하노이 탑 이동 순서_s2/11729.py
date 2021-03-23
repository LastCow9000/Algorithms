# boj 11729 하노이 탑 이동 순서 s2
# noj.am/11729

def hanoi(start, dest, n):
    if n == 1:
        print(f'{start} {dest}')
        return
    hanoi(start, 6 - start - dest, n - 1)
    print(f"{start} {dest}")
    hanoi(6 - start - dest, dest, n - 1)


N = int(input())
print((1 << N) - 1)  # 2^N - 1
hanoi(1, 3, N)


'''
절차적말고 귀납적으로 생각해보자!

1. 함수의 정의
    void func(int start, int dest, int n)
    원판 n개를 start 기둥에서 dest 기둥으로 옮기는 방법을 출력하는 함수 
2. base condition
    n = 1 일 때 print(start + " " + dest)
3. 재귀 식
    - n - 1 개의 원판을 2번 기둥에 옮기고 n번째 원판을 3번 기둥에 옮기면 된다.
    - 1, 2, 3 번 기둥이므로 번호의 합은 6이다.
    - n - 1 개의 원판을 옮길 때 횟수를 A라고 한다면 n 개의 원판을 옮긴느 횟수는
      n - 1 개의 원판을 2번 기둥에 옮기고(A번) n번 째 기둥을 3번 기동으로 옮기고(1번)
      다시 n - 1 개의 원판을 2번에서 3번 기둥으로 옮기면(A번) 2A + 1번이다.


    n - 1개의 원판을 기둥 start에서 6-start-dest로 옮긴다. func(start, 6-start-dest, n-1)
    n번 원판을 기둥 start에서 dest로 옮긴다. print(start + " " + dest)
    n - 1개의 원판을 기둥 6-start-dest에서 dest로 옮긴다. func(6-start-dest, dest, n-1)
'''
