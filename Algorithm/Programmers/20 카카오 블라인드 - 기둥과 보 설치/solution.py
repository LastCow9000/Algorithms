# Programmers 2020 KAKAO BLIND RECRUITMENT - 기둥과 보 설치 Lv3
# https://programmers.co.kr/learn/courses/30/lessons/60061

# 기둥 - 바닥 위/      보 한쪽 끝 위    / 기둥 위
#        y == 0 / (x-1, y)보 , (x, y)보 / (x, y-1)기
# 보 - 한쪽 끝 기둥 위          / 양 끝 보
#      (x, y-1)기, (x+1, y-1)기 / (x-1, y)보 && (x+1, y)보

def check(res):
    for x, y, a in res:
        if a == 0: # 기둥
            if y == 0 or (x - 1, y, 1) in res or (x, y, 1) in res or (x, y - 1, 0) in res:
                continue
            else:
                return False
        else: # 보
            if (x, y - 1, 0) in res or (x + 1, y - 1, 0) in res or ((x - 1, y, 1) in res and (x + 1, y, 1) in res):
                continue
            else:
                return False
        
    return True


def solution(n, build_frame):
    res = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 0: # 삭제
            res.remove(item)
            if not check(res): # 삭제 or 설치 후 모든 것을 체크해보고 조건에 부합하지 않으면 롤백
                res.add(item)
        else: # 설치
            res.add(item)
            if not check(res):
                res.remove(item)

    res = list(map(list, res))
    res.sort(key=lambda x:(x[0], x[1], x[2]))
    return res

if __name__ == "__main__":
    n1, build_frame1 = 5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    n2, build_frame2 = 5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
    # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
    # print(solution(n1, build_frame1))
    print(solution(n2, build_frame2))