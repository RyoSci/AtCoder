# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
tot = [0]*(n+1)
for i in range(n):
    tot[i+1] += tot[i]+a[i]
tot.append(INF)
ans = "No"
for x_pos in range(n):
    x = tot[x_pos]
    y_pos = bisect_left(tot, x+p)
    if tot[y_pos] != x+p:
        continue
    y = tot[y_pos]
    z_pos = bisect_left(tot, y+q)
    if tot[z_pos] != y+q:
        continue
    z = tot[z_pos]
    w_pos = bisect_left(tot, z+r)
    if tot[w_pos] != z+r:
        continue
    else:
        ans = "Yes"
        break

print(ans)
