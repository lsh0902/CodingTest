N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for i in range(N)]

dirs= [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0],
]

def solution(arr):
    visited = [[False for i in range(M)] for j in range(N)]
    q = [[0,0,1]]
    visited[0][0] = True
    cnt = 0
    while q:
        y, x, cnt = q.pop(0)
        if y == N-1 and x == M-1:
            return cnt
        for dir in dirs:
            ny = y + dir[0]
            nx = x + dir[1]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and arr[ny][nx] == 1:
                visited[ny][nx] = True
                q.append([ny,nx, cnt +1])

answer = solution(arr)
print(answer)