# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())
g = [set() for i in range(n)]
for i in range(n):
    g[i].add(i)
now = n

for _ in range(q):
    querry = list(map(int, input().split()))
    if querry[0] == 1:
        u, v = querry[1:]
        u -= 1
        v -= 1
        if len(g[u]) == 1:
            now -= 1
        if len(g[v]) == 1:
            now -= 1
        g[u].add(v)
        g[v].add(u)
    else:
        v = querry[1]
        v -= 1
        if len(g[v]) != 1:
            for e in g[v]:
                if e != v:
                    g[e].remove(v)
                    if len(g[e]) == 1:
                        now += 1
            g[v] = set()
            g[v].add(v)
            now += 1

    print(now)
