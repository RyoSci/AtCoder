n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]


def find(x):
    if p[x] == -1:
        return x
    p[x] = find(p[x])
    return p[x]


def unite(x, y):
    if find(x) == find(y):
        return
    p[find(x)] = find(y)
    return


res = 0
for i in range(m):
    p = [-1]*n
    for j in range(m):
        if i == j:
            continue
        unite(ab[j][0]-1, ab[j][1]-1)
    d = [0]*n
    for j in range(n):
        d[find(j)] += 1
    if max(d) != n:
        res += 1

print(res)
