# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

seen = [0]*n

k = 0


def dfs(par, root=-1):
    global k
    k += 1
    if k >= 10**6:
        print(10**6)
        exit()
    for chi in g[par]:
        if chi == root:
            continue
        if seen[chi] == 1:
            continue
        seen[chi] = 1
        dfs(chi, par)
        seen[chi] = 0


seen[0] = 1
dfs(0)
print(k)
