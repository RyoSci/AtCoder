# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
c = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(n):
    for j in range(9):
        tmp = i+c[j]
        if tmp <= n:
            if dp[tmp] < dp[i]*10+j+1:
                dp[tmp] = dp[i]*10+j+1

ans = 0
for i in range(n+1):
    ans = max(ans, dp[i])

print(ans)
