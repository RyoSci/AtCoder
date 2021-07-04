n, m = map(int, input().split())

p = [x for x in range(n)]


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    if find(x) == find(b):
        return
    p[find(x)] = find(y)


for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    union(a, b)

for i in range(n):
    p[i] = find(i)

print(len(set(p))-1)
