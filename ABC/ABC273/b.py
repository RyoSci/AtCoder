# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, k = map(int, input().split())

for i in range(k):
    now = x % (10**(i+1))
    if now >= 5*(10**i):
        x += 10**(i+1)
        x -= now
    else:
        x -= now

print(x)
