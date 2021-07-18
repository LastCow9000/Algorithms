# boj 4659 비밀번호 발음하기 s5
# noj.am/4659

vowel = ['a', 'e', 'i', 'o', 'u']

def check3ConsecutiveLetter(password): # 연속된 3모음 or 3자음 체크
    for i in range(len(password) - 2): # 글자 길이가 5글자라면 앞의 글자는 3번째 글자까지만 봐주면 됨(ex: 012, 123, 234)
        vowel_cnt = 0
        consonant_cnt = 0
        prev = ''

        for j in range(i, i + 3):
            if prev == '':
                prev = password[j]
                            
            if password[j] not in vowel: # 자음이면
                consonant_cnt += 1
                if prev in vowel: # 이전 글자가 모음이면 자음 갯수 초기화
                    consonant_cnt = 0
            
            if password[j] in vowel: # 모음이면
                vowel_cnt += 1
                if prev not in vowel:
                    vowel_cnt = 0
            
            if consonant_cnt >= 3 or vowel_cnt >= 3:
                return False

            prev = password[j]

    return True


def check2ConsecutiveLetter(password):
    
    prev = ''
    for c in password:
        if prev == '':
            prev = c
            continue
        
        if c == prev and (c != 'e' and c != 'o'): # 연속된 글자거나 ee, oo 가 아니면
            return False

        prev = c

    return True

def checkInVowel(password):
    flag = False

    for c in password:
        if c in vowel:
            flag = True
        
    return flag


while True:
    password = input()
    if password == 'end':
        break

    flag1 = check3ConsecutiveLetter(password)
    flag2 = check2ConsecutiveLetter(password)
    flag3 = checkInVowel(password)
    flag = flag1 and flag2 and flag3

    print(f'<{password}> is acceptable.') if flag else print(f'<{password}> is not acceptable.')
