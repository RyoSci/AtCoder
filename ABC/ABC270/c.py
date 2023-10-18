# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = []


def dfs(par, root=-1):
    ans.append(par+1)
    if par == y:
        print(*ans)
        exit()
    for chi in g[par]:
        if chi == root:
            continue
        dfs(chi, par)
    ans.pop()


dfs(x)
