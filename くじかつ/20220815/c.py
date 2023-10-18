# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
ans = 0
MOD = 998244353
for i in range(20):
    if pow(10, i) <= n < pow(10, i+1):
        tmp = n-pow(10, i)+1
        ans += tmp*(tmp+1)//2
        ans %= MOD

    elif pow(10, i+1) <= n:
        tmp = pow(10, i+1)-pow(10, i)
        ans += tmp*(tmp+1)//2
        ans %= MOD
print(ans)
