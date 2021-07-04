def solution(A,B):
    answer = 0
    # 하나는 오름차순 다른 하나는 내림차순으로 정렬해서 곱해준다
    A.sort()
    B.sort(reverse = True)
    answer = sum([x * y for x, y in zip(A, B)])
    return answer


if __name__ == "__main__":
    A1, B1 = [1, 4, 2], [5, 4, 4]	# 29
    A2, B2 = [1,2], [3,4] # 10
    print(solution(A1, B1))
    print(solution(A2, B2))