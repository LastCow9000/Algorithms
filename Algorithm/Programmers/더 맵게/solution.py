# 더 맵게 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1 and scoville[0] < K:
        sum_sv = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, sum_sv)
        cnt += 1
    if len(scoville) != 0 and scoville[0] >= K:
        return cnt
    return -1


if __name__ == "__main__":
    scoville, K = [1, 2, 3, 9, 10, 12],	7
    print(solution(scoville, K))
