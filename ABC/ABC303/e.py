# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


def dfs(par, root=-1):
    global terminal
    flag = True
    for chi in g[par]:
        if chi == root:
            continue
        flag = False
        dfs(chi, par)

    if flag:
        terminal = par


# 端を見つける
terminal = -1
dfs(0)


ans = []


def dfs1(par, root=-1, from_center=2):
    if from_center == 0:
        ans.append(len(g[par]))
    for chi in g[par]:
        if chi == root:
            continue
        dfs1(chi, par, (from_center+1) % 3)


dfs1(terminal)

ans.sort()

print(*ans)
