# boj 1713 후보 추천하기 s2
# noj.am/1713
from collections import deque

N = int(input())
recommend_cnt = int(input())
recom_student_list = list(map(int, input().split()))
dq = deque() # 오래된 것부터 빠져나가기 위해 큐 사용
recom_student = dict() # 학생의 추천수를 저장하기 위한 해시

for stu_num in recom_student_list:
    if len(dq) < N: # 액자의 갯수보다 적으면 큐에 학생번호 넣고 사전에서도 cnt + 1
        if stu_num in dq: # 이미 액자에 있는 학생번호면 사전 cnt만 + 1
            recom_student[stu_num] += 1
            continue
        dq.append(stu_num)
        recom_student[stu_num] = 1
    elif stu_num in dq: # 액자틀 갯수가 넘었는데 이미 액자에 있는 학생일 경우 사전 cnt만 + 1
        recom_student[stu_num] += 1
    else: # 액자틀 갯수 초과 시 사전에서 추천수가 젤 적은 학생 삭제 및 큐에서 제거
        recom_min = [k for k, v in recom_student.items() if v == min(recom_student.values())]
        if len(recom_min) > 1:
            for num in dq:
                if num in recom_min:
                    dq.remove(num)
                    del(recom_student[num])
                    dq.append(stu_num)
                    recom_student[stu_num] = 1
                    break
        else:
            dq.remove(recom_min[0])
            del(recom_student[recom_min[0]])
            dq.append(stu_num)
            recom_student[stu_num] = 1

print(*sorted(dq))
