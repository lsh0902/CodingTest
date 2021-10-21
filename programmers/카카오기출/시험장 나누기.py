import sys
from itertools import combinations

sys.setrecursionlimit(10000)


def findRoot(tree, current):
    isRoot = True
    for i in range(len(tree)):
        if current in tree[i]:
            parent = i
            isRoot = False
            break
    if isRoot:
        return current
    else:
        return findRoot(tree, parent)


# def treeOrder():

def solution(k, num, links):
    if k == 1: return sum(num)

    def preorder(nodeNum):
        visited[nodeNum] = True
        if len(tree[nodeNum]) == 0:
            return num[nodeNum]
        elif len(tree[nodeNum]) == 1:
            return num[nodeNum] + preorder(tree[nodeNum][0])
        return num[nodeNum] + preorder(tree[nodeNum][0]) + preorder(tree[nodeNum][1])
    def getSum(i):
        root = findRoot(tree, i)
        return preorder(root)

    answer = 100000000000000
    nodes = len(num)
    edges = []
    for idx, i in enumerate(links):
        if i[0] != -1:
            edges.append([idx, i[0]])
        if i[1] != -1:
            edges.append([idx, i[1]])

    combs = combinations([i for i in range(len(num)-1)], nodes - k)

    for comb in combs:
        # tree 만들기
        tree = [[] for i in range(nodes)]
        visited = [False for i in range(nodes)]
        for j in comb:
            tree[edges[j][0]].append(edges[j][1])
        maximum = 0
        for i in range(nodes):
            if not visited[i]:
                mysum = getSum(i)
                maximum = max(maximum, mysum)
        answer = min(answer, maximum)
    return answer
print(solution(3,[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],	[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
print(solution(1,[6, 9, 7, 5],[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(2,[6, 9, 7, 5],[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(4,[6, 9, 7, 5],[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))


