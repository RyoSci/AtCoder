import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = [[]*n for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

c = sorted(list(map(int, input().split())), reverse=True)
print(sum(c)-c[0])
order = [-1]*n
cnt = 0
order[0] = cnt


def dfs(pair, root=-1):
    global cnt
    for chi in g[pair]:
        if chi == root:
            continue
        cnt += 1
        order[chi] = cnt
        dfs(chi, pair)


dfs(0)

res = [0]*n
for i in range(n):
    res[i] = c[order[i]]

print(*res)
