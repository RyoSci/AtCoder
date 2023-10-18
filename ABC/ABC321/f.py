# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

q, k = map(int, input().split())
mod = 998244353
dp = [0]*(k+1)
dp[0] = 1
ans = []
for i in range(q):
    cat, x = map(str, input().split())
    x = int(x)
    if cat == "+":
        for j in range(k, 0, -1):
            if j-x >= 0:
                dp[j] += dp[j-x]
                dp[j] %= mod
    else:
        for j in range(0, k):
            if j+x <= k:
                dp[j+x] -= dp[j]
                dp[j+x] %= mod

    ans.append(dp[k])

print(*ans)
