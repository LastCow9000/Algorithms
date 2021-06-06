# programmers 위장 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    _dict = {}
    ans = 1

    for cloth in clothes:
        _dict.setdefault(cloth[1], 0)
        _dict[cloth[1]] += 1
    
    # (안입는 경우 + 한 가지씩 입는경우) * (안입는 경우 + 한 가지씪 입는경우) - 모두 안입는 경우(1)
    for i in [key + 1 for key in _dict.values()]:
        ans *= i
    return ans - 1

if __name__ == "__main__":
    solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])