# 2019 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방 lv2
# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    # 나은 풀이
    idNick = {}
    history = []

    for rec in record:
        recs = rec.split()
        if recs[0] == "Enter":
            history.append((recs[1], "님이 들어왔습니다."))
            idNick[recs[1]] = recs[2]
        elif recs[0] == "Leave":
            history.append((recs[1], "님이 나갔습니다."))
        else:
            idNick[recs[1]] = recs[2]

    return [idNick[dt[0]] + dt[1] for dt in history]
    '''
    # 첫 풀이
    result = []
    idNick = {}
    order = []
    for string in record:
        info = string.split()
        if len(info) == 3:
            behavior, uid, nick = info[0], info[1], info[2]
        else:
            behavior, uid = info[0], info[1]
        if behavior == "Enter":
            idNick[uid] = nick
            order.append(uid)
        elif behavior == "Leave":
            order.append("-" + uid)
        else:
            idNick[uid] = nick

    for uid in order:
        if uid.count("-"):
            result.append(f'{idNick[uid[1:]]}님이 나갔습니다.')
        else:
            result.append(f'{idNick[uid]}님이 들어왔습니다.')

    return result
    '''


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
              "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    print(solution(record))

'''
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
'''
