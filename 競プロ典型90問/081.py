import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())

# grid = [[0]*(55) for _ in range(55)]
grid = [[0]*(5005) for _ in range(5005)]
for i in range(n):
    a, b = map(int, input().split())
    grid[a][b] += 1

# for i in range(55):
    # for j in range(54):
for i in range(5005):
    for j in range(5004):
        grid[i][j+1] += grid[i][j]

ans = 0
# for j in range(1, 55-k):
for j in range(1, 5005-k):
    res = 0
    for i in range(1, k+2):
        res += grid[i][k+j] - grid[i][j-1]
    ans = max(ans, res)

    # for i in range(k+2, 55):
    for i in range(k+2, 5005):
        res += grid[i][k+j]-grid[i][j-1]
        res -= grid[i-k-1][k+j]-grid[i-k-1][j-1]
        ans = max(ans, res)

print(ans)
