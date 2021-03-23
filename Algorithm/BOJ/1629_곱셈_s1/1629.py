# boj 1629 곱셈 s1
# noj.am/1629

def recursive(A, B, C):
    if B <= 1:  # 기본 조건
        return A % C
    val = recursive(A, B // 2, C)
    val = val * val % C  # 만약 2^n mod 6이 2라면 2^2n mod 6은 2*2 = 4이다
    if B % 2 == 1:  # 홀수면 한 번 더 곱해줌
        return val * A % C
    return val


A, B, C = map(int, input().split())
print(recursive(A, B, C))
