from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())
ver_edges = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    ver_edges[a].append(b)
    ver_edges[b].append(a)

res = 0


def dfs(grand, pair, i):
    global res
    children = ver_edges[pair]
    tmp = [0, 0]

    for chi in children:
        if chi == grand:
            continue
        cnt = dfs(pair, chi, i+1)
        tmp.append(cnt)
    tmp.sort(reverse=True)
    # print(i, tmp)
    res = max(res, tmp[0]+tmp[1])

    return max(tmp)+1


dfs(-1, 0, 0)
print(res + 1)
