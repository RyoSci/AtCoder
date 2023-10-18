# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, y, z = map(int, input().split())


ans = INF
# ハンマー使わない
if x*y < 0:
    ans = min(ans, abs(x))
else:
    if abs(x) < abs(y):
        ans = min(ans, abs(x))

# ハンマー使う
if z*y < 0:
    ans = min(ans, abs(z)+abs(x-z))
else:
    if abs(z) < abs(y):
        ans = min(ans, abs(z)+abs(x-z))

if ans == INF:
    print(-1)
else:
    print(ans)
