# K번째수 lv1
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        slice_sort_array = sorted(array[commands[i][0] - 1 : int(commands[i][1])])
        answer.append(slice_sort_array[commands[i][2] - 1])
    return answer


if __name__ == "__main__":
    array, commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	# [5, 6, 3]
    print(solution(array, commands))