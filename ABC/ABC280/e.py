# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, p = map(int, input().split())
MOD = 998244353

dp = [-1]*(n+1)
dp[n] = 0

for i in range(n, 0, -1):
    if dp[i] == -1:
        continue
    if dp[max(0, i-2)] == -1:
        dp[max(0, i-2)] = 0
    dp[max(0, i-2)] += (dp[i]+1) * p * pow(100, MOD-2, MOD)
    dp[max(0, i-2)] %= MOD
    if dp[max(0, i-1)] == -1:
        dp[max(0, i-1)] = 0
    dp[max(0, i-1)] += (dp[i]+1) * 1 - (dp[i]+1) * p * pow(100, MOD-2, MOD)
    dp[max(0, i-1)] %= MOD

print((dp[1]+1) % MOD)
# print(dp)
