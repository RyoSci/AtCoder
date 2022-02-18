n = int(input())
dp = [100001] * 100001
dp[0] = 0
nine = [9 ** i for i in range(1, 7)]
six = [6 ** i for i in range(1, 8)]


for i in range(1, n + 1):
    for j in nine:
        if j <= i:
            dp[i] = min(dp[i - j] + 1, dp[i])
        else:
            break
    for j in six:
        if j <= i:
            dp[i] = min(dp[i - j] + 1, dp[i])
        else:
            break
    dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[n])
