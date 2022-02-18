import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s_ = input().strip()
s = []
for i in s_:
    if i == "?":
        s.append(-1)
    else:
        s.append(int(i))

n = len(s)
dp = [[0]*13 for _ in range(n+1)]
dp[0][0] = 1

mod = 10**9+7
for i in range(n):
    for j in range(13):
        if dp[i][j] == 0:
            continue
        if s[i] == -1:
            for k in range(10):
                # tmp = pow(10, n-i-1, 13)*k % 13
                # tmp = (tmp+j) % 13
                tmp = (10*j+k) % 13
                dp[i+1][tmp] += dp[i][j]
                dp[i+1][tmp] %= mod
        else:
            # tmp = pow(10, n-i-1, 13)*int(s[i]) % 13
            # tmp = (tmp+j) % 13
            tmp = (10*j+int(s[i])) % 13
            dp[i+1][tmp] += dp[i][j]
            dp[i+1][tmp] %= mod

print(dp[-1][5] % mod)
