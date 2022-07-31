# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
MOD = 10**9+7

n, p = map(int, input().split())

if n == 1:
    print(p-1)
else:
    ans = p-1
    ans *= pow(p-2, n-1, MOD)
    print(ans % MOD)
