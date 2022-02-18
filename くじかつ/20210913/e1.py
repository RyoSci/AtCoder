import numpy as np
from numba import jit
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


@jit
def main():
    r, c, k = map(int, input().split())
    # r, c, k = 2000, 2000, 2*10**5
    grid = [[0]*(c+2) for _ in range(r+2)]
    grid = np.zeros((r+2, c+2))

    for i in range(k):
        ri, ci, vi = map(int, input().split())
        # ri, ci, vi = 1, 1, 1
        ri -= 1
        ci -= 1
        grid[ri][ci] = vi

    # dp = [[[0]*4 for j in range(c+2)] for i in range(r+2)]
    dp = np.zeros((r+2, c+2, 4))

    for i in range(r+1):
        for j in range(c+1):
            for k in range(3, 0, -1):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1]+grid[i][j])
            for k in range(4):
                dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k])
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k])

    ans = 0
    for k in range(4):
        ans = max(ans, dp[r-1][c-1][k])

    return int(ans)


print(main())
