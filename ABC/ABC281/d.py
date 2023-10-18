# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

N, K, D = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[-1]*D for j in range(K+1)] for i in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            # 使う
            if j+1 <= K:
                nk = k+a[i]
                nk %= D
                dp[i+1][j+1][nk] = max(dp[i+1][j+1][nk], dp[i][j][k] + a[i])

            # 使わない
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])


print(dp[N][K][0])

# for i in range(N):
#     for j in range(K):
#         print(i, j, *dp[i][j])
