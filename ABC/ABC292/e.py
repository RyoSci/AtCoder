# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
u = [0]*m
v = [0]*m
edges = [[0]*n for _ in range(n)]
inputs = [[] for _ in range(n)]
outputs = [[] for _ in range(n)]
for i in range(n):
    edges[i][i] = 1
for i in range(m):
    u[i], v[i] = map(lambda x: int(x)-1, input().split())
    edges[u[i]][v[i]] = 1
    # edges[v[i]][u[i]] = 1

    outputs[u[i]].append(v[i])
    inputs[v[i]].append(u[i])

seen = [0]*n
tp = []


def dfs(par):
    seen[par] = 1

    for chi in outputs[par]:
        if seen[chi]:
            continue
        dfs(chi)

    tp.append(par)


for i in range(n):
    if seen[i]:
        continue
    dfs(i)

ans = 0
for c in tp:
    for i in inputs[c]:
        for j in outputs[c]:
            if i == j:
                continue
            if edges[i][j]:
                continue
            ans += 1
            edges[i][j] = 1
            outputs[i].append(j)
            inputs[j].append(i)

print(ans)
