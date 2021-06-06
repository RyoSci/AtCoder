import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())

# roads = [[i, (i+1) % n] for i in range(n)]
roads = [[] for i in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    roads[a].append(b)

res = 0


def dfs(pare):
    children = roads[pare]
    for chi in children:
        if chi not in tmp:
            tmp.add(chi)
            dfs(chi)


for i in range(n):
    tmp = set()
    tmp.add(i)
    dfs(i)
    res += len(tmp)

print(res)
