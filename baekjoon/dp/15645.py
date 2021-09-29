import sys
input = sys.stdin.readline
N = int(input())

dp = [[0 for i in range(3)] for j in range(2)]
smalldp = [[0 for i in range(3)] for j in range(2)]

for i in range(0, N):
    arr = list(map(int, input().split()))
    for j in range(3):
        if j == 0:
            dp[1][j] = arr[j] + max(dp[0][j], dp[0][j+1])
            smalldp[1][j] = arr[j] + min(smalldp[0][j], smalldp[0][j + 1])
        elif j == 1:
            dp[1][j] = arr[j] + max(dp[0][j], dp[0][j-1], dp[0][j+1])
            smalldp[1][j] = arr[j] + min(smalldp[0][j], smalldp[0][j-1], smalldp[0][j+1])
        else:
            dp[1][j] = arr[j] + max(dp[0][j], dp[0][j-1])
            smalldp[1][j] = arr[j] + min(smalldp[0][j], smalldp[0][j-1])
    for j in range(3):
        dp[0][j] = dp[1][j]
        smalldp[0][j] = smalldp[1][j]

print(max(dp[-1]), min(smalldp[-1]))