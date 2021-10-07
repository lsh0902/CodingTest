"""
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [[0 for i in range(M+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + arr[i-1][j-1] - dp[i-1][j-1]

orders = []
for i in range(int(input())):
    orders.append(list(map(int, input().split())))

for y,x,y2,x2 in orders:
    # print(f'{dp[y2][x2]} + {dp[y-1][x-1]} - {dp[y2][x - 1]} - {dp[y - 1][x2]} = {dp[y2][x2] + dp[y-1][x-1] - dp[y2][x-1] - dp[y-1][x2]}')
    print(dp[y2][x2] + dp[y-1][x-1] - dp[y2][x-1] - dp[y-1][x2])


