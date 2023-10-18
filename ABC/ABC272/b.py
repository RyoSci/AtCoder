# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for i in range(m):
    k, *x = list(map(int, input().split()))
    for j in range(k):
        for l in range(k):
            g[x[j]-1][x[l]-1] = 1

ans = "Yes"
for i in range(n):
    if sum(g[i]) != n:
        ans = "No"
        break

print(ans)
