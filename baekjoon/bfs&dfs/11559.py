"""
백준 11559 뿌요뿌요
"""
answer = 0
arr = [input() for _ in range(12)]
for i in range(12) :
    arr[i] = list(arr[i])


def bfs(i, j, visited) :
    target = arr[i][j]
    q = [[i,j]]
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    ret = [[i,j]]
    while q :
        y ,x = q.pop(0)
        for dir in dirs:
            nextY, nextX = y+dir[0], x+dir[1]
            if nextX >=0 and nextX < 6 and nextY >=0 and nextY < 12 and arr[nextY][nextX] == target and not visited[nextY][nextX]:
                visited[nextY][nextX] = True
                q.append([nextY, nextX])
                ret.append([nextY, nextX])
    return ret

def ppuyo(nums) :
    for i, j in nums :
        arr[i][j] = '0'

def downBlock():

    # arr 에서 0 확인
    for x in range(6):
        count = 0
        for y in range(11,-1,-1):
            if arr[y][x] == '0' :
                count += 1
        if count > 0 :
            cur = 11
            for y in range(11,-1,-1):
                if arr[y][x] != '0':
                    arr[cur][x] = arr[y][x]
                    cur -= 1
            for y in range(cur, -1, -1):
                arr[y][x] = '.'

    # for i in arr:
    #     print(i)
loop = True
while loop :
    loop = False
    visited = [[False for _ in range(6)] for _ in range(12)]
    for i in range(12) :
        for j in range(6) :
            if arr[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                numArr = bfs(i, j,visited)
                if len(numArr) >= 4:
                    loop = True
                    ppuyo(numArr)
                    downBlock()
    if loop :
        answer += 1
print(answer)

