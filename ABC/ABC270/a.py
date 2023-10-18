# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())
c = [0]*3
for i in range(3):
    c[i] += a % 2
    a //= 2
    c[i] += b % 2
    b //= 2

ans = 0

for i in range(3):
    if c[i] > 0:
        ans += 2**i

print(ans)
