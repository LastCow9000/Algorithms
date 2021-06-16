# programmers 카펫 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
# -2 씩 한 것 곱하면 옐로우 수가 나온다
    answer = []
    yellow_h = int(yellow ** 0.5)
    # 가로 >= 세로 이므로 세로는 루트 이하의 값이 나온다
    while yellow_h >= 1:
        yellow_w = yellow // yellow_h
        
        brown_h = yellow_h + 2
        brown_w = yellow_w + 2
        
        if (brown_h * brown_w) == brown + yellow:
            answer.append(brown_w)
            answer.append(brown_h)
            break
            
        yellow_h -= 1

    return answer

if __name__ == "__main__":
    brown1, yellow1 = 10, 2
    brown2, yellow2 = 8, 1
    brown3, yellow3 = 24, 24
    print(solution(brown1, yellow1))
    print(solution(brown2, yellow2))
    print(solution(brown3, yellow3))