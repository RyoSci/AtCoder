# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import combinations
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, t, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0


def dfs(i):
    global ans
    if i == n:
        ans += 1
        return
    if seen[i]:
        dfs(i+1)
        return

    for ti in range(t):
        if i < group[ti]:
            continue
        flag = True
        for ng in g[i]:
            if teams[ti][ng]:
                flag = False
                break
        if flag:
            teams[ti][i] = 1
            dfs(i+1)
            teams[ti][i] = 0


ans = 0
for group in combinations(range(n), t):
    teams = [[0]*n for _ in range(t)]
    for gi in range(t):
        teams[gi][group[gi]] = 1

    seen = [0]*n
    for gg in group:
        seen[gg] = 1

    dfs(0)

print(ans)
