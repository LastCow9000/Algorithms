def solution(s):
    ans = 1000
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):  # 반을 넘어서까지 비교할 필요x
        cnt = 1
        c = s[:i]  # 맨 앞에서부터 일정 갯수만큼 자름
        tmpStr = ""

        for j in range(i, len(s), i):  # 자를 갯수만큼 뛰어넘음
            if c == s[j:j+i]:
                cnt += 1
            else:  # 자른 문자열이 다르다면 더해주기
                if cnt == 1:
                    cnt = ""
                tmpStr += (str(cnt) + c)
                cnt = 1
                c = s[j:j+i]  # 다음 문자열을 탐색하기 위한 초기화

        if cnt > 1:
            tmpStr += (str(cnt) + c)
        else:
            tmpStr += c

        ans = min(ans, len(tmpStr))

    return ans
