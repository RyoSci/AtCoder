s = input()
dp = [[0]*(len(s)+1) for _ in range(9)]

chokudai = "chokudai"

for j in range(len(s)):
    if s[j] == "c":
        dp[1][j+1] += 1
    dp[1][j+1] += dp[1][j]

mod = 10**9+7
for i in range(1, 8):
    for j in range(len(s)):
        dp[i+1][j+1] += dp[i+1][j]
        if s[j] == chokudai[i]:
            dp[i+1][j+1] += dp[i][j]
        dp[i+1][j+1] %= mod

print(dp[-1][-1])
