# boj 1343 폴리오미노 s4
# noj.am/1343

board = list(input())
xCnt = 0
dotCnt = 0
res = []
ans = []
flag = True

for i in range(len(board)):
    if board[i] == "X":  # X면 xcnt++
        # X이고 .카운트가 한개라도 있을 시 X전에 .이 있다. 음수로 리스트에 추가해서 x카운트와 구분하고 .카운트 초기화
        if dotCnt > 0:
            res.append(-dotCnt)
            dotCnt = 0
        xCnt += 1
    elif board[i] == ".":  # .이면 dotcnt++
        if xCnt > 0:  # .인데 앞에 x가 존재할시 양수로 추가하여 dotcnt(음수)와 구분
            res.append(xCnt)
            xCnt = 0
        dotCnt += 1
    if i == len(board) - 1:  # 리스트 끝까지 다돌았을 경우 값 추가
        res.append(xCnt)
        res.append(-dotCnt)

for cnt in res:  # xcnt와 dotcnt로 갯수를 판단해서 결과값 뽑아내기
    if cnt > 0 and cnt % 2 == 0:  # 짝수일 경우 폴리오미노로 뒤덮을수 있다.
        A = cnt // 4
        B = cnt % 4 // 2
        ans.append(("AAAA" * A) + ("BB" * B))
    elif cnt < 0:  # dot 카운트 일경우 . 추가
        ans.append("." * abs(cnt))
    elif cnt > 0 and cnt % 2 == 1:  # xcnt가 홀수면 불가
        flag = False

print("".join(ans)) if flag else print(-1)
