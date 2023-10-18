# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()
ans = INF
for l in range(n-k+1):
    ans = min(ans, h[l+k-1]-h[l])

print(ans)
