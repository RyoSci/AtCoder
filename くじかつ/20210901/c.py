import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, s = input().split()
n = int(n)

dp = [[0]*(n+1) for _ in range(4)]
t = "ATCG"
for i in range(n):
    for j in range(4):
        if s[i] == t[j]:
            dp[j][i+1] += 1
        dp[j][i+1] += dp[j][i]

res = 0
for l in range(0, n):
    for r in range(l+2, n+1, 2):
        a = dp[0][r]-dp[0][l]
        t = dp[1][r]-dp[1][l]
        c = dp[2][r]-dp[2][l]
        g = dp[3][r]-dp[3][l]
        if a == t and c == g:
            res += 1

print(res)
