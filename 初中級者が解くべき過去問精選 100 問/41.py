d, n = map(int, input().split())

tmp = [int(input()) for _ in range(d)]

min_max = [[100, 0] for _ in range(d)]

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(d):
        if a <= tmp[j] <= b:
            min_max[j][0] = min(min_max[j][0], c)
            min_max[j][1] = max(min_max[j][1], c)

dp = [[0, 0] for _ in range(d)]
for i in range(d-1):
    for j in range(2):
        dp[i+1][j] = max(dp[i][0]+abs(min_max[i+1][j]-min_max[i][0]),
                         dp[i][1]+abs(min_max[i+1][j]-min_max[i][1]))

print(max(dp[d-1]))
