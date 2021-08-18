# boj 17609 회문 s1
# noj.am/17609
import sys; inp = sys.stdin.readline

def last_check(l, r, string):
    while l < r:
        if string[l] != string[r]: # 1개 제거만 유사회문이므로 2개는 x
            return False
        l += 1
        r -= 1
    return True


def is_pseudo_palindrome(l, r, string):
    while l < r:
        if string[l] == string[r]:
            l += 1
            r -= 1

        else: # 두개를 한 포인터씩 이동해서 다시 체크
            res1 = last_check(l + 1, r, string) 
            res2 = last_check(l, r - 1, string)
        
            if res1 or res2: # 둘 중 하나라도 유사회문이면 True
                return True
            return False

    return False


    '''acbdddbcba 판단 불가'''
    # l = 0
    # r = len(string) - 1 # 투포인터로 O(N) 시도
    # cnt = 0
    # flag = False
    # while l < r:
    #     if string[l] == string[r]: # 같으면 같이 이동
    #         l += 1
    #         r -= 1
    #         continue

    #     if string[l] != string[r]: # 같지 않다면 한개씩 이동해보고 같으면 해당 포인터를 이동
    #         cnt += 1 # 제거한 글자 갯수
    #         if cnt == 2: # 한 개까지만
    #             break
    #         if string[l + 1] == string[r]:
    #             l += 1
    #         elif string[l] == string[r - 1]:
    #             r -= 1
    #         else: # 양 쪽 포인터를 한개씩 움직여봐도 같지 않다면 유사 회문도 만족x
    #             break

    # else: # 반복문을 정상적으로 마쳤다면 회문
    #     flag = True

    # return flag 


    ''' 시간초과 (pop -> O(N))'''
    # for i in range(len(string)): 
    #     temp = list(string) # pop메서드를 사용하기 위해 리스트화
    #     temp.pop(i) # 한글자씩 제거하고 
    #     temp = ''.join(temp) # 문자열로 다시 바꾼 후
    #     if temp == temp[::-1]: # 회문인지 판별
    #         return True
    # return False



for _ in range(int(input())):
    ans = 2
    string = inp().rstrip()
    if string == string[::-1]:
        ans = 0
    elif is_pseudo_palindrome(0, len(string) - 1, string):
        ans = 1
    print(ans)

