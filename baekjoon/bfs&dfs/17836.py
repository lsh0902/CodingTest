"""
17836 백준
"""

from collections import deque
H, W, T = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(H)]
dirs = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0]
]
def bfs():
    visited = [[False for i in range(W)] for j in range(H)]
    visitSword = [[False for i in range(W)] for j in range(H)]
    q = deque([[0,0,0,0]])
    visited[0][0] = True
    while q:
        y, x, t, sword = q.popleft()
        if y == H -1 and x == W-1:
            if t > T:
                print("Fail")
            else:
                print(t)
            return
        if sword :
            for i in range(2):
                ny = y + dirs[i][0]
                nx = x + dirs[i][1]
                if 0 <= ny < H and 0 <= nx < W and not visitSword[ny][nx]:
                    visitSword[ny][nx] = True
                    q.append([ny,nx,t+1,1])
        else :
            for i in range(4):
                ny = y + dirs[i][0]
                nx = x + dirs[i][1]
                if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] != 1 and not visited[ny][nx]:
                    if arr[ny][nx] == 2:
                        visitSword[ny][nx] = True
                        q.append([ny, nx, t + 1, 1])
                    else:
                        visited[ny][nx] = True
                        q.append([ny, nx, t + 1, 0])
    print("Fail")
bfs()