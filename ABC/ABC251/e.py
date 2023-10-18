# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
dp = [[INF]*2 for _ in range(n)]

ans = INF

dp[0][0] = 0
dp[0][1] = a[0]

for i in range(n-1):
    # 使っていない
    dp[i+1][1] = min(dp[i+1][1], dp[i][0]+a[i+1])
    # 使っている
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+a[i+1])
    dp[i+1][0] = min(dp[i+1][0], dp[i][1])

now = 0
# flag = False
for i in range(n-1, 0, -1):
    if now == 0:
        now ^= 1

    else:
        if dp[i-1][now] == dp[i][now]-a[i]:
            # flag = True
            continue
        else:
            now ^= 1

if now == 1:
    ans = min(dp[n-1][0], dp[n-1][1])
else:
    ans = min(dp[n-1][0]+a[-1], dp[n-1][1])

# print(dp)
print(ans)
