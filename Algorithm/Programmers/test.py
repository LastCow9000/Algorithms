def solution(s):
    if s == s[::-1]:
        return len(s)

    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                ans = max(ans, len(s[i:j]))
    
    return ans


s1 = "abcdcba" # 7
s2 = "abacde" # 3
print(solution(s1))
print(solution(s2))