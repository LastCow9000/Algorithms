# boj 4358 생태학 g4
# noj.am/4358

from collections import defaultdict
import sys

trees = defaultdict(int)

while True:
    inputTree = sys.stdin.readline().rstrip()
    if not inputTree:  # 입력이 끝나면 반복문 빠져나감
        break
    trees[inputTree] += 1  # 해당 트리를 입력받을때마다 갯수(value) 1개씩 증가

totaltree = sum(trees.values())  # 전체 트리의 갯수
treeName = sorted(trees.keys())  # 키(나무이름)만 따서 정렬하고 리스트로 반환
for tree in treeName:  # tree이름과 사전에서 tree이름(key)으로 갯수(value)뽑아와서 계산 후 출력
    print("%s %.4f" % (tree, trees[tree] / totaltree * 100))

    # print(f"{tree} {round(trees[tree] / totaltree * 100, 4)}") 이렇게 했더니 틀림
