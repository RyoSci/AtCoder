import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

r, c, k = map(int, input().split())
grid = [[0]*c for _ in range(r+1)]

for i in range(k):
    ri, ci, vi = map(int, input().split())
    # ri-=1
    ci -= 1
    grid[ri][ci] = vi

dp = [[[0, [0, 0]] for j in range(c)] for i in range(r+1)]

for i in range(r):
    for j in range(c-1):
        dp[i+1][j][0] = dp[i][j][0]+sum(dp[i][j][1])
        dp[i+1][j][1].append(grid[i+1][j])
        dp[i][j][1].append(grid[i][j+1])

        # dp[i][j][1].sort(reversed=True)
        dp[i][j][1].sort()
        dp[i][j][1] = dp[i][j][1][::-1]
        dp[i][j][1].pop()
        if dp[i][j][0]+sum(dp[i][j][1]) > dp[i][j+1][0]+sum(dp[i][j+1][1]):
            dp[i][j+1] = dp[i][j][:]
    j += 1
    dp[i+1][j][0] = dp[i][j][0]+sum(dp[i][j][1])
    dp[i+1][j][1].append(grid[i+1][j])

for j in range(c-1):
    dp[r][j][1].append(grid[r][j+1])
    # dp[r][j][1].sort(reversed=True)
    dp[r][j][1].sort()
    dp[r][j][1] = dp[r][j][1][::-1]
    dp[r][j][1].pop()
    if dp[r][j][0]+sum(dp[r][j][1]) > dp[r][j+1][0]+sum(dp[r][j+1][1]):
        dp[r][j+1] = dp[r][j][:]

print(dp[r][c-1][0]+sum(dp[r][c-1][1]))
