from collections import deque

def solution(skill, skill_trees):
    skillList = set(skill)
    cnt = 0

    for st in skill_trees:
        tmpStr = ''
        st = deque(list(st))
        while st: # 순서에 있는 스킬들만 뽑아서 찍어본다
            tmpChar = st.popleft()
            if tmpChar in skillList:
                tmpStr += tmpChar

        idx = 0
        while idx < len(tmpStr): # 내가 찍은 스킬트리와 스킬 순서를 앞부터 한글자 씩 비교
            if skill[idx] != tmpStr[idx]:
                break
            idx += 1
        else:
            cnt += 1

    return cnt

if __name__ == "__main__":
    skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees)) # 2