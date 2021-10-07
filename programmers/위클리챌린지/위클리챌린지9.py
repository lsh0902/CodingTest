from collections import defaultdict
def TreeSize(start, excep, linkInfo, n):
    q = list(filter(lambda x: x != excep , linkInfo[start]))
    visited = [True if i in q else False for i in range(n+1)]
    visited[start] = True
    cnt = len(q) + 1

    while q:
        nextVal = q.pop()
        for i in linkInfo[nextVal]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def solution(n, wires):
    linkInfo = defaultdict(list)
    for i, j in wires:
        linkInfo[i].append(j)
        linkInfo[j].append(i)
    minimum = 100000000
    for i, j in wires:
        minVal = abs(TreeSize(i, j, linkInfo, n) - TreeSize(j, i, linkInfo, n))
        if minVal < minimum:
            minimum = minVal
    return minimum