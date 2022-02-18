n, m = map(int, input().split())
dp = [1] * (n + 1)

for i in range(m):
    blank = int(input())
    dp[blank] = 0

for i in range(2, n + 1):
    if dp[i] != 0:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    else:
        pass

print(dp[-1])