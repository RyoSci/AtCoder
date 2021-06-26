import sys
sys.setrecursionlimit(10**6)

m = int(input())
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]


def dfs(i, j, cnt):
    global res
    for ii, jj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        if 0 <= i+ii < n and 0 <= j+jj < m and area[i+ii][j+jj] == 1:
            if (i+ii, j+jj) not in memo:
                memo.add((i+ii, j+jj))
                res = max(res, cnt+1)
                dfs(i+ii, j+jj, cnt+1)
    memo.remove((i, j))


res = 0
for i in range(n):
    for j in range(m):
        memo = set()
        if area[i][j] == 1:
            memo.add((i, j))
            res = max(res, 1)
            dfs(i, j, 1)

print(res)
