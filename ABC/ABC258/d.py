# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**20

n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

ans = INF
now = 0
for i in range(n):
    if i+1 > x:
        break
    now += a[i]+b[i]
    res = (x-i-1)*b[i]+now
    ans = min(ans, res)

print(ans)
