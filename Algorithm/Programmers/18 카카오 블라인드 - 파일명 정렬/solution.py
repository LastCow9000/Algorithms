# Programmers 2020 KAKAO BLIND RECRUITMENT - [3차]파일명 정렬 Lv2
# https://programmers.co.kr/learn/courses/30/lessons/17686

#files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#res = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress",
         "A-10 Thunderbolt II", "F-14 Tomcat"]
#res = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]


def HEAD(file):  # head와 나머지 부분 구하기
    length = len(file)
    for i in range(length):
        if file[i].isdigit():  # file의 i번째 문자가 숫자라면 i-1번째까지 slicing해서 head와 나머지 부분으로 분리
            return [file[:i], file[i:]]


def NUMBER(string):  # number와 tail 구하기
    length = len(string)
    for i in range(length):
        # string의 i번째 문자가 숫자가 아니라면 i-1까지 slicing해서 number 반환(tail은 안쓰므로 반환x)
        if not string[i].isdigit():
            return string[:i]
    return string  # string 문자열을 다 탐색했는데도 숫자라면 string 자체가 number다


def solution(files):
    res = []

    for file in files:
        hn = HEAD(file)
        n = NUMBER(hn[1])
        res.append((hn[0], n, file))  # head, number, 결과값을 위해 file 을 tuple로 삽입

    # 파이썬은 stable sort, head를 소문자로 바꿔서 1차정렬 그 후 number기준 정렬
    res.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [s[2] for s in res]  # 정렬된 리스트에서 file 반환


if __name__ == "__main__":
    print(solution(files))
