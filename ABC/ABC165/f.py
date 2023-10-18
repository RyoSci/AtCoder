# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

b = []
pre = [-1]*n
ans = [0]*n


def dfs(par, root=-1):
    pos = bisect_left(b, a[par])
    popflag = False
    if pos == len(b):
        popflag = True
        b.append(a[par])
    else:
        pre[par] = b[pos]
        b[pos] = a[par]

    ans[par] = len(b)

    for chi in g[par]:
        if chi == root:
            continue
        dfs(chi, par)

    if popflag:
        b.pop()
    else:
        b[pos] = pre[par]


dfs(0)

print(*ans)
