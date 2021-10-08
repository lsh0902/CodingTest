def dfs(positions, row) :
    n = len(positions)
    if n == row:
        return 1
    count = 0
    possibleCol = possible(positions, row)
    for col in possibleCol :
        positions[row] = col
        count += dfs(positions, row + 1)
    return count


def possible(pos, row) :
    ret = [True for i in range(len(pos))]
    for i in range(len(pos)) :
        for j in range(row):
            if pos[j] == i or (row-j == abs(pos[j] - i)):
                ret[i] = False
    return [idx for idx, i in enumerate(ret) if i]


def solution(n):
    ans = [0] * n
    return dfs(ans, 0)

print(solution(10))