import tempfile


# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

ans = 0
for i in range(1, 10**6):
    j = str(i)*2
    j = int(j)
    if j <= n:
        ans += 1

print(ans)
