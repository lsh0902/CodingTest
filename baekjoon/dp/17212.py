N = int(input())
dp = [100000000 for i in range(N+1)]
dp[0] = 0
moneys = [7,5,2,1]

for i in range(1, N+1):
    for money in moneys:
        if money <= i and dp[i-money]+1 < dp[i]:
            dp[i] = dp[i-money]+1
print(dp[-1])