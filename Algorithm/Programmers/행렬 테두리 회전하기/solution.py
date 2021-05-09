# 행렬 테두리 회전하기 lv2
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    arr = [[] for i in range(rows)]
    cnt = 0
    ans = []
    for i in range(1, rows * columns + 1):
        if i % columns == 1:
            cnt += 1
        arr[cnt - 1].append(i)

    for querie in queries:
        x1, y1, x2, y2 = querie[0] - 1, querie[1] - \
            1, querie[2] - 1, querie[3] - 1
        tmp_arr = arr[x1][y1]
        minVal = tmp_arr

        for x in range(x1, x2):
            arr[x][y1] = arr[x + 1][y1]
            val = arr[x][y1]
            minVal = min(minVal, val)

        for y in range(y1, y2):
            arr[x2][y] = arr[x2][y + 1]
            val = arr[x2][y]
            minVal = min(minVal, val)

        for x in range(x2, x1, -1):
            arr[x][y2] = arr[x - 1][y2]
            val = arr[x][y2]
            minVal = min(minVal, val)

        for y in range(y2, y1, -1):
            arr[x1][y] = arr[x1][y - 1]
            val = arr[x1][y]
            minVal = min(minVal, val)

        arr[x1][y1 + 1] = tmp_arr
        ans.append(minVal)

    return ans


if __name__ == "__main__":
    rows1 = 6
    columns1 = 6
    queries1 = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    rows2 = 3
    columns2 = 3
    queries2 = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
    rows3 = 100
    columns3 = 97
    queries3 = [[1, 1, 100, 97]]
    print(solution(rows1, columns1, queries1))
    print(solution(rows2, columns2, queries2))
    print(solution(rows3, columns3, queries3))
