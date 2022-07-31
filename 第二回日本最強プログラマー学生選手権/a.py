# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, y, z = map(int, input().split())
for i in range(10**6):
    if z*y > i*x:
        ans = i

print(ans)
