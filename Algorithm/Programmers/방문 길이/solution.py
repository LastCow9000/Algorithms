# 방문 길이 lv2
# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    pos = [0, 0]
    histories = []
    
    for d in dirs:
        
        if d == "U":
            if pos[1] < 5: # 범위내면 이동
                pos[1] += 1
                history = [pos[0], pos[1] - 1, pos[0], pos[1]]
                reverseHistory = [pos[0], pos[1], pos[0], pos[1] - 1] # 0, 0 에서 -> 5, 5로 간다면 5, 5에서 0, 0으로 가는 것도 기록
                if not history in histories and not reverseHistory in histories: # 가지 않은 경로라면 ++
                    answer += 1
                    histories.append(history)
                    histories.append(reverseHistory)

        elif d == "D":
            if pos[1] > -5:
                pos[1] -= 1
                history = [pos[0], pos[1] + 1, pos[0], pos[1]]
                reverseHistory = [pos[0], pos[1], pos[0], pos[1] + 1]
                if not history in histories and not reverseHistory in histories: 
                    answer += 1
                    histories.append(history)
                    histories.append(reverseHistory)
                
        elif d == "R":
            if pos[0] < 5:
                pos[0] += 1
                history = [pos[0] - 1, pos[1], pos[0], pos[1]]
                reverseHistory = [pos[0], pos[1], pos[0] - 1, pos[1]]
                if not history in histories and not reverseHistory in histories: 
                    answer += 1
                    histories.append(history)
                    histories.append(reverseHistory)
                
        elif d == "L":
            if pos[0] > -5:
                pos[0] -= 1
                history = [pos[0] + 1, pos[1], pos[0], pos[1]]
                reverseHistory = [pos[0], pos[1], pos[0] + 1, pos[1]]
                if not history in histories and not reverseHistory in histories:
                    answer += 1
                    histories.append(history)
                    histories.append(reverseHistory)
    
    return answer