# programmers 이진 변환 반복하기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    cnt = 0
    zeroCnt = 0
    while len(s) != 1:
        zeroCnt += s.count("0")
        s = s.replace('0','')
        s = str(format(len(s), 'b'))
        cnt += 1
    answer.append(cnt)
    answer.append(zeroCnt)

    return answer

if __name__ == "__main__":
    s1 = "110010101001" # [3,8]
    s2 = "01110" # [3,3]
    s3 = "1111111" # [4,1]
    print(solution(s1))
    print(solution(s2))
    print(solution(s3))
