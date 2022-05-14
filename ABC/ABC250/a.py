# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1

ans = 0
for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    nr = r+x
    nc = c+y
    if 0 <= nr < h and 0 <= nc < w:
        ans += 1

print(ans)
