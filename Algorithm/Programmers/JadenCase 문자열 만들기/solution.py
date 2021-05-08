# JadenCase 문자열 만들기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    ans = ''
    if s[0].isdigit():
        ans += s[0]
    else:
        ans += s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == " ":
            ans += s[i].upper()
            continue
        ans += s[i].lower()
    return ans


if __name__ == "__main__":
    s1 = "3people unFollowed me"
    s2 = "for the last week"
    print(solution(s1))
    print(solution(s2))
