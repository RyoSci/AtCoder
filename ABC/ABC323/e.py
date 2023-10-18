# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

mod = 998244353


n, x = map(int, input().split())
t = list(map(int, input().split()))

inv = pow(n, -1, mod)
# inv = 1/n

dp = [0] * (x+2)
dp[0] = 1
ans = 0

for i in range(x+1):
    if dp[i] == 0:
        continue
    for j in range(n):
        ni = i + t[j]
        if j == 0 and i <= x < ni:
            ans += dp[i] * inv
            ans %= mod
        elif ni <= x+1:
            dp[ni] += dp[i] * inv
            dp[ni] %= mod

print(ans % mod)
