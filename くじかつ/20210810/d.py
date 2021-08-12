from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())

g = [[] for _ in range(n)]

ab = []
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)
    ab.append((a, b))


color_num = 0

for i in range(n):
    color_num = max(color_num, len(g[i]))

ans = dict()


def dfs(pair, root, color):
    for chi in g[pair]:
        if chi == root:
            continue
        color += 1
        color %= color_num
        ans[(pair, chi)] = color+1
        ans[(chi, pair)] = color+1
        dfs(chi, pair, color)


dfs(0, -1, -1)

print(color_num)
for i in range(n-1):
    a, b = ab[i]
    if (a, b) in ans:
        print(ans[(a, b)])
    else:
        print(ans[(b, a)])
