import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)


def dfs(par, root=-1):
    global ans
    for chi in g[par]:
        if chi == root:
            continue
        if seen[chi] == 1:
            continue
        seen[chi] = 1
        ans += 1
        dfs(chi, par)


ans = 0
for i in range(n):
    seen = [0]*n
    seen[i] = 1
    ans += 1

    dfs(i)

print(ans)
