from collections import defaultdict
import sys

sys.setrecursionlimit(30000)


def dfs(curNode, tree, visited, a):
    global answer
    visited[curNode] = True
    for child in tree[curNode]:
        if not visited[child]:
            a[curNode] += dfs(child, tree, visited, a)

    answer += abs(a[curNode])
    return a[curNode]


def solution(a, edges):
    if sum(a) != 0: return -1

    global answer
    answer = 0
    tree = defaultdict(list)
    visited = [False for i in range(len(a))]

    for root, child in edges:
        tree[root].append(child)
        tree[child].append(root)

    visited[0] = True
    dfs(0, tree, visited, a)

    return answer