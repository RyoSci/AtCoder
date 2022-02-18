from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)

res = 0
for i in range(n):
    d = deque()
    d.append(i)
    tmp = [0]*n
    tmp[i] = 1
    while len(d) != 0:
        pare = d.popleft()
        for chi in g[pare]:
            if tmp[chi] == 0:
                tmp[chi] = 1
                d.append(chi)
    res += sum(tmp)

print(res)
