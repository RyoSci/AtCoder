import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, w = map(int, input().split())
dp = [[[0 for k in range(3*100+10)] for j in range(n+1)] for i in range(n+1)]

wv = [list(map(int, input().split())) for _ in range(n)]

w1 = wv[0][0]
# i番目までの品物を見てj個選んだときの重さが w1*j+k のときの価値の最大
for i in range(n):
    wi, vi = wv[i]
    for j in range(n):
        for k in range(301):
            # 取らない
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

            # 取る
            tmp = w1*(j+1)+k+wi-w1
            if tmp <= w:
                dp[i+1][j+1][k+wi-w1] = max(dp[i+1]
                                            [j+1][k+wi-w1], dp[i][j][k]+vi)


res = 0
for j in range(n+1):
    for k in range(301):
        res = max(res, dp[n][j][k])

print(res)
