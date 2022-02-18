import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

mod = 998244353

n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

seen = [0]*n
finished = [0]*n


def dfs(pair, root=-1):
    global flag, ans
    seen[pair] = 1
    for chi in g[pair]:
        if chi == root:
            continue
        if seen[chi] == 1 and finished[chi] == 0:
            flag = True
            ans += 1
        elif seen[chi] == 1:
            continue
        else:
            dfs(chi, pair)
    finished[pair] = 1


ans = 0

for i in range(n):
    if seen[i] == 1:
        continue
    flag = False
    dfs(i, -1)
    if not flag:
        print(0)
        exit()

if ans == 0:
    print(0)
else:
    print(pow(2, ans, mod))
