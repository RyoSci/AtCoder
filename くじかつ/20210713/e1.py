h, w, k_ = map(int, input().split())

dp = [[0]*w for _ in range(h+1)]
dp[0][0] = 1
mod = 10**9+7

for i in range(h):
    for j in range(w):
        for k in range(1 << (w-1)):
            flag = True
            for l in range(1, w-1):
                if k >> l & 1 and k >> (l-1) & 1:
                    flag = False
                    break
            if not flag:
                continue
            if 0 <= j-1 and k >> (j-1) & 1 == 1:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= mod
            elif j+1 < w and k >> j & 1 == 1:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod
            else:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod

print(dp[h][k_-1])
