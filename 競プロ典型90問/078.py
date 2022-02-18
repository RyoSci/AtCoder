n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

res = 0
for i in range(n):
    cnt = 0
    for chi in g[i]:
        if chi < i:
            cnt += 1
    if cnt == 1:
        res += 1
print(res)
