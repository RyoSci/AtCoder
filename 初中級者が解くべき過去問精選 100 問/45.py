import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

for i in range(10**8):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    c = [int(input()) for _ in range(m)]
    y = [int(input()) for _ in range(n)]

    INF = 10**18
    dp = [[INF]*256 for _ in range(n)]
    for k in c:
        j = 128
        nj = j+k
        if 0 <= nj <= 255:
            if dp[0][nj] > 0+(y[0]-(j+k))**2:
                dp[0][nj] = (y[0]-(j+k))**2
        elif nj > 255:
            if dp[0][255] > (y[i]-255)**2:
                dp[0][255] = (y[i]-255)**2
        else:
            if dp[0][0] > (y[i]-0)**2:
                dp[0][0] = (y[i]-0)**2

    # i番目がの値がjとなるときのsum(yi - yi-1)^2 の最小値
    for i in range(1, n):
        for j in range(256):
            if dp[i-1][j] == INF:
                continue
            for k in c:
                nj = j+k
                if 0 <= nj <= 255:
                    if dp[i][nj] > dp[i-1][j] + (y[i]-nj)**2:
                        dp[i][nj] = dp[i-1][j]+(y[i]-nj)**2
                elif nj > 255:
                    if dp[i][255] > dp[i-1][j] + (y[i]-255)**2:
                        dp[i][255] = dp[i-1][j]+(y[i]-255)**2
                else:
                    if dp[i][0] > dp[i-1][j] + (y[i]-0)**2:
                        dp[i][0] = dp[i-1][j]+(y[i]-0)**2

    print(min(dp[n-1]))
