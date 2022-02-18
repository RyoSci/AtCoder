q = int(input())
for _ in range(q):
    x = input()
    y = input()
    n = len(x)
    m = len(y)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] < dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            if dp[i][j] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1]
            if x[i-1] == y[j-1]:
                if dp[i][j] < dp[i-1][j-1]+1:
                    dp[i][j] = dp[i-1][j-1]+1
    print(dp[n][m])
