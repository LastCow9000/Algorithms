# 2019 KAKAO BLIND RECRUITMENT - 매칭 점수 lv3
# https://programmers.co.kr/learn/courses/30/lessons/42893
import re

# 기본점수: 검색어(word)가 등장하는 횟수
# 외부 링크 수 : a 태그의 링크 수
# 링크점수 : 해당 웹 페이지로 링크가 걸린 다른 웹페지들의 sum(웹페이지의 기본점수 / 외부 링크수)
# 매칭점수 : 기본점수 + 링크점수
# 매칭점수가 가장 높은 것(2 순위 인덱스가 젤 작은것)

def parse_html(word, page):
    reg_url = re.compile('(?:<meta property="og:url" content="https:\/\/([\w\.\/\?]+)"\/>)')
    reg_external_link = re.compile('<a href="https:\/\/([\w\.\/\?]+)">')
    reg_search_word = re.compile('([a-z]+)[^a-z]', re.I)
    url = reg_url.search(page).group(1)
    external_link = reg_external_link.findall(page)
    word_list = reg_search_word.findall(page)

    basic_score = 0
    for w in word_list:
        if w.lower() == word.lower():
            basic_score += 1

    return url, external_link, basic_score

def solution(word, pages):
    ans = -1
    parsed_pages = {}
    link_scores = {}

    # page 파싱해서 기본점수, 외부 링크 구하기
    for idx, page in enumerate(pages):
        url, external_link, basic_score = parse_html(word, page)
        parsed_pages[url] = [external_link, basic_score, idx]

    # 링크점수 구하기
    for key, val in parsed_pages.items():
        basic_score = val[1]
        external_link_cnt = len(val[0])
        
        for ex_link in val[0]:
            link_scores.setdefault(ex_link, 0) 
            link_scores[ex_link] += basic_score / external_link_cnt

    # 매칭점수 구해서 최대값 뽑기
    max_score = -1
    for key, val in parsed_pages.items():
        basic_score = val[1]
        idx = val[2]
        link_score = link_scores[key] if key in link_scores.keys() else 0

        match_score = basic_score + link_score
        if match_score > max_score:
            max_score = match_score
            ans = idx
    
    return ans
            
if __name__ == "__main__":
    word1 = 'blind'
    pages1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    word2 = 'Muzi'
    pages2 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    print(solution(word1, pages1))
    print(solution(word2, pages2))
