import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, w = map(int, input().split())
dp = [dict() for _ in range(n+1)]
dp[0][0] = 0

wv = [list(map(int, input().split())) for _ in range(n)]

# i番目までの品物を選んだときの、重さがjのときの価値の最大値
for i in range(n):
    wi, vi = wv[i]
    for dpwi in dp[i].keys():
        # 取らない
        if dpwi not in dp[i+1]:
            dp[i+1][dpwi] = dp[i][dpwi]
        else:
            dp[i+1][dpwi] = max(dp[i+1][dpwi], dp[i][dpwi])

        # 取る
        if dpwi + wi not in dp[i+1]:
            dp[i+1][dpwi+wi] = dp[i][dpwi]+vi
        else:
            dp[i+1][dpwi+wi] = max(dp[i+1][dpwi+wi], dp[i][dpwi]+vi)


res = 0
for key, val in dp[n].items():
    if key <= w:
        res = max(res, val)

print(res)
