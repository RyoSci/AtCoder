s = int(input())
dp = [1]*(2000+1)
dp[0], dp[1], dp[2] = 0, 0, 0

mod = 10**9+7
for i in range(3, s+1):
    for j in range(3, s):
        if i - j >= 3:
            if j < 6:
                dp[i] = (dp[i] + dp[j] * dp[i-j]) % mod
            else:
                dp[i] = (dp[i] + dp[i-j]) % mod
print(dp[s])
# print(dp)
