# programmers 최댓값과 최솟값 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    nums = list(map(int, s.split()))
    return f"{min(nums)} {max(nums)}"