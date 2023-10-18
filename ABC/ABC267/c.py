# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))

tot = [0]*(n+1)
for i in range(n):
    tot[i+1] += tot[i]+a[i]


now = 0
for i in range(m):
    now += a[i]*(i+1)

ans = now
for i in range(n-m):
    now -= tot[i+m]-tot[i]
    now += a[i+m]*(m)
    ans = max(ans, now)

print(ans)
