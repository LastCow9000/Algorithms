# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

def solution(A, B):
    cnt = 1
    prev_end = 0
    if not A:
        return 0
    for i in range(len(A)):
        if A[i] > B[prev_end]:
            cnt += 1
            prev_end = i
    return cnt


if __name__ == "__main__":
    print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))
    print(solution([], []))
    print(solution([1], [5]))
    print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 9]))
