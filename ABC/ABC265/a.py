# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, y, n = map(int, input().split())

ans = INF
for i in range(n):
    rest = n-i*3
    if rest >= 0:
        ans = min(ans, i*y+rest*x)

print(ans)
