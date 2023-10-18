# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

dp = [[0]*n for _ in range(50)]

for j in range(n):
    dp[0][j] = a[j]-1

for i in range(49):
    for j in range(n):
        dp[i+1][j] = dp[i][dp[i][j]]

ans = [0] * n
for j in range(n):
    ans[dp[49][j]] = 1

# print(dp[-1])
# print(ans)
print(sum(ans))
