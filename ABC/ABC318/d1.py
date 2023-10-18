# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
d = []
for i in range(n-1):
    di = list(map(int, input().split()))
    d.append(di)


m = 1 << n

dp = [0] * m

for mask in range(m):
    for i in range(n):
        if mask >> i & 1:
            continue
        for j in range(i+1, n):
            if mask >> j & 1:
                continue

            nmask = mask | (1 << i) | (1 << j)

            dp[nmask] = max(dp[nmask], dp[mask]+d[i][j-i-1])


ans = 0
for i in range(m):
    ans = max(ans, dp[i])

print(ans)
