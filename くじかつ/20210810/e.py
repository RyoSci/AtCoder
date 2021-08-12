from sys import setrecursionlimit
setrecursionlimit(10**7)
n, m = map(int, input().split())
g = [[] for _ in range(m)]

for i in range(n):
    k, *l = map(int, input().split())
    for li in l:
        g[li-1].append(i)

p = [i for i in range(n)]


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False


def unite(x, y):
    if same(x, y):
        return
    p[find(x)] = find(y)
    return


for i in range(m):
    if len(g[i]) < 2:
        continue
    for j in range(1, len(g[i])):
        unite(g[i][0], g[i][j])

ans = "YES"
for i in range(n):
    p[i] = find(p[i])
    if not same(p[0], p[i]):
        ans = "NO"
        break

print(ans)
