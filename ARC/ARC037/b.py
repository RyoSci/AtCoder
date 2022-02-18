n, m = map(int, input().split())
edges = [[] for _ in range(n)]

for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    edges[u].append(v)
    edges[v].append(u)


def dfs(pair, root):
    global p, flag
    children = edges[pair]
    for chi in children:
        if chi == root:
            continue
        if p[chi] != -1:
            flag = False
        else:
            p[chi] = pair
            dfs(chi, pair)


p = [-1] * n
res = 0
for i in range(n):
    if p[i] != -1:
        continue
    p[i] = i
    flag = True
    dfs(i, i)
    if flag:
        res += 1

print(res)
