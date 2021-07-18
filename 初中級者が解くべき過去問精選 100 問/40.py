n, k = map(int, input().split())
dp = [[0]*3 for _ in range(n)]
decided = dict()
for i in range(k):
    a, b = map(int, input().split())
    decided[a-1] = b-1

if 0 in decided:
    dp[0][decided[0]] = 1
else:
    for i in range(3):
        dp[0][i] = 1
if 1 in decided:
    for j in range(3):
        dp[1][decided[1]] += dp[0][j]
else:
    for i in range(3):
        for j in range(3):
            dp[1][i] += dp[0][j]

for i in range(2, n):
    for j in range(3):
        for l in range(3):
            if j == l:
                continue
            if i in decided and decided[i] == l or i not in decided:
                dp[i][l] += dp[i-1][j]
                dp[i][l] %= 10**4
                if dp[i-1][l] == 0:
                    continue
                dp[i][l] += dp[i-2][j]
                dp[i][l] %= 10**4

print(sum(dp[-1]) % 10**4)
