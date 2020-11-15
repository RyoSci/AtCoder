x = int(input())
dp = [0] * (x + 1)
dp[0] = 1
for i in range(x + 1):
    if dp[i] == 1:
        for j in range(100, 106):
            if i + j <= x:
                dp[i + j] = 1

print(dp[-1])
