h, w = map(int, input().split())
s = [input() for _ in range(h)]
dp = [[0 for _ in range(w)] for _i in range(h)]

for i in range(h - 1, -1, -1):
    for j in range(w - 1, -1, -1):
        if i == h - 1 and j == w - 1:
            continue
        elif i == h - 1:
            dp[i][j] = dp[i][j + 1] + (s[i][j] != s[i][j + 1])
        elif j == w - 1:
            dp[i][j] = dp[i + 1][j] + (s[i][j] != s[i + 1][j])
        else:
            dp[i][j] = min(dp[i][j + 1] + (s[i][j] != s[i][j + 1]),
                           dp[i + 1][j] + (s[i][j] != s[i + 1][j]))

res = (dp[0][0] + (s[0][0] != ".") + 1) // 2
print(res)
