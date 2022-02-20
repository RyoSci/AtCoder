import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
g=[[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)

now=1
ans=[[] for _ in range(n)]
def dfs(par, root=-1):
    global now
    ans[par].append(now)
    chi_num=0
    for chi in g[par]:
        if chi==root:
            continue
        dfs(chi,par)
        chi_num+=1
        now+=1
    
    if chi_num>=1:
        now-=1
        ans[par].append(now)
    else:
        ans[par].append(now)

dfs(0)

for i in range(n):
    print(*ans[i])