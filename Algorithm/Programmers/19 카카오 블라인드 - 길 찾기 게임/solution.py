# 2019 KAKAO BLIND RECRUITMENT - 길 찾기 게임 lv3
# https://programmers.co.kr/learn/courses/30/lessons/42892
import sys
sys.setrecursionlimit(int(1e6))

class Tree:
    def __init__(self, data_list):
        self.data = max(data_list, key=lambda x:x[1]) # y값이 가장 높은 것이 루트
        left_list = list(filter(lambda x:x[0] < self.data[0], data_list)) # 부모보다 작으면 lc
        right_list = list(filter(lambda x:x[0] > self.data[0], data_list)) # 부모보다 크면 rc

        if len(left_list):
            self.left_child = Tree(left_list)
        else:
            self.left_child = None

        if len(right_list):
            self.right_child = Tree(right_list)
        else:
            self.right_child = None

def order(node, pre_order, post_order):
    pre_order.append(node.data)

    if node.left_child is not None:
        order(node.left_child, pre_order, post_order)

    if node.right_child is not None:
        order(node.right_child, pre_order, post_order)

    post_order.append(node.data)


def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    pre_order = []
    post_order = []

    order(root, pre_order, post_order)

    answer.append(list(map(lambda x: nodeinfo.index(x)+1 , pre_order)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 , post_order)))

    return answer


if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    print(solution(nodeinfo)) # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]