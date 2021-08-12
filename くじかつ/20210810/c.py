n, m = map(int, input().split())
a = set()
for i in range(m):
    ai = int(input())
    a.add(ai)

dp = [0]*(n+1)
dp[0] = 1
mod = 10**9+7

for i in range(n):
    if i+1 <= n and i+1 not in a:
        dp[i+1] += dp[i]
        dp[i+1] %= mod
    if i+2 <= n and i+2 not in a:
        dp[i+2] += dp[i]
        dp[i+2] %= mod

print(dp[n])
