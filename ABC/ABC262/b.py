# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
uv = [[0]*n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv[u][v] = 1
    uv[v][u] = 1

ans = 0
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            if uv[a][b]*uv[b][c]*uv[c][a] == 1:
                ans += 1

print(ans)
