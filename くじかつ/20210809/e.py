n, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

dp = [[0]*(t+1) for _ in range(n+1)]

res = 0
for i in range(n):
    for j in range(t+1):
        if j+ab[i][0] <= t:
            dp[i+1][j+ab[i][0]] = max(dp[i+1][j+ab[i][0]], dp[i][j]+ab[i][1])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    res = max(res, dp[i][t-1]+ab[i][1])

# for i in range(n+1):
#     print(dp[i])

"""
嘘解法 after contestでWA
選択する集合の中で最大の料理を最後にとれないケースがある。

# j = t-1
# noused = []
# for i in range(n, 0, -1):
#     if dp[i][j] == dp[i-1][j]:
#         noused.append(i-1)
#     else:
#         j -= ab[i-1][0]

# max_bi = 0
# for i in noused:
#     max_bi = max(ab[i][1], max_bi)

# print(max(dp[n][t], dp[n][t-1]+max_bi))

# print(noused)
"""

print(res)
