# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[INF]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
    g[b][a] = 1

dp = [[0]*n for _ in range(1 << n)]
# dp[i][j]:=集合iまで見て、最終jにいる時の通り数
dp[1][0] = 1
for i in range(1 << n):
    for j in range(n):
        for k in range(n):
            if g[j][k] == INF:
                continue
            # 集合iの状態でjからkに行く
            # jが含まれていない時とkを既に通った時はパスする
            if not ((i >> j) & 1) or (i >> k) & 1:
                continue
            dp[i | (1 << k)][k] += dp[i][j]

print(sum(dp[(1 << n) - 1]))
# print(dp)
