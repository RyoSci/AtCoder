from sys import modules


k = int(input())
mod = 10**9+7


dp = [0]*(k+1)
dp[0] = 1

for i in range(1, k+1):
    index = min(i, 9)
    for j in range(1, index+1):
        dp[i] += dp[i-j]
        dp[i] %= mod

if k % 9 == 0:
    print(dp[k])
else:
    print(0)
