"""
Knapsack
"""
import sys
input = sys.stdin.readline
N, maxWeight = map(int, input().split())
w, v = [], []
for i in range(N):
    w1, v1 = map(int, input().split())
    w.append(w1)
    v.append(v1)

dp = [[0 for i in range(maxWeight + 1)] for j in range(N)]
for i in range(N):
    for j in range(1, maxWeight + 1):
        if j < w[i]: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
print(dp[-1][-1])