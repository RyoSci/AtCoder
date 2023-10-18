import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    g[a].append((b, c))
    g[b].append((a, c))


def dfs(par, now=0):
    global ans
    ans = max(ans, now)
    for chi, c in g[par]:
        if seen[chi]:
            continue
        seen[chi] = 1
        dfs(chi, now+c)
        seen[chi] = 0


seen = [0]*n
ans = 0
for i in range(n):
    seen[i] = 1
    dfs(i)
    seen[i] = 0

print(ans)
