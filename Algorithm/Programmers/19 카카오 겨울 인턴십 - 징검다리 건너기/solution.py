# 2019 카카오 개발자 겨울 인턴십 - 징검다리 건너기 lv3
# https://programmers.co.kr/learn/courses/30/lessons/64062

def cntStone(target, stones, k):  # 징검다리 건널 수 있는지 체크하는 함수
    now = -1  # 시작지점은 징검다리 밖이므로
    next = 0  # 징검다시 시작지점 인덱스 0번

    while next < len(stones):  # 마지막 징검다리 인덱스전까지만
        if stones[next] >= target:  # 건널 수 있는 사람의 수보다 돌에 써진 수가 크거나 같다면
            now = next
            next += 1
        else:  # 사람수가 돌 숫자보다 많다면
            next += 1
        if next - now > k:  # 뛰어넘을 수 있는 수보다 크다면 못 건넌다
            return False

    return True


def solution(stones, k):
    left = 1
    right = int(2e8)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if cntStone(mid, stones, k):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
