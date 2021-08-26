n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*(w+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = 0


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def lcm(x, y):
    return x*y//gcd(x, y)


for i in range(n):
    for j in range(w+1):
        if dp[i][j] >= 0:
            tmp = lcm(j, wv[i][0])
            if tmp < w+1:
                dp[i+1][tmp] = max(dp[i+1][tmp], dp[i][j]+wv[i][1])
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])

res = 0
for i in range(n+1):
    for j in range(w+1):
        res = max(res, dp[i][j])

print(res)
