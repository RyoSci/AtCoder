from sys import setrecursionlimit
setrecursionlimit(10**6)

n, q = map(int, input().split())
g = [-1]*n


def find(x):
    if g[x] == -1:
        return x
    g[x] = find(g[x])
    return g[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    if same(x, y):
        return
    g[find(x)] = find(y)
    return


for i in range(q):
    c, x, y = map(int, input().split())
    if c == 0:
        unite(x, y)
    else:
        if same(x, y):
            print(1)
        else:
            print(0)
