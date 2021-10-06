def solution(money):
    arrlength = len(money)
    dp = [0] * arrlength
    dp[0] = money[0]
    for i in range(1, len(money) - 1):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])

    answer = dp[arrlength - 2]
    print(dp)
    print(answer)

    dp = [0] * arrlength
    dp[1] = money[1]
    for i in range(1, len(money)):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])

    print(dp[arrlength - 1])
    answer = dp[arrlength - 1] if dp[arrlength - 1] > answer else answer
    return answer

print(solution(	[90, 0, 0, 95, 1, 1]))