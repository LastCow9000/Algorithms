# boj 5671 호텔 방 번호 s4
# noj.am/5671

while True:
    try:
        cnt = 0
        N, M = map(int, input().split())

        for num in range(N, M + 1):
            for i in range(len(str(num))):
                # 숫자를 문자로 변경 후 특정 문자가 문자열에 2개이상 존재하는 경우 반복되므로 no count
                if str(num).count(str(num)[i]) > 1:
                    break
            else:  # break가 안되고 for문이 종료되면 실행
                cnt += 1

        print(cnt)

    except EOFError:
        break
