import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w, k = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))

# dp[i][j]<-i回目のときに、jのエリアにいる通り数
dp = [[0, 0, 0, 0] for _ in range(k+1)]
mod = 998244353

# dp[i][2]<-x,yが同じ
# dp[i][0]<-xが同じ
# dp[i][1]<-yが同じ
# dp[i][3]<-その他
if x1 == x2:
    if y1 == y2:
        dp[0] = [1, 1, 1, 0]
    else:
        dp[0] = [1, 0, 0, 0]
else:
    if y1 == y2:
        dp[0] = [0, 1, 0, 0]
    else:
        dp[0] = [0, 0, 0, 1]


for i in range(k):
    a, b, c, d = dp[i]
    na = a*(w-1)+b+d-c
    na %= mod
    nb = b*(h-1)+a+d-c
    nb %= mod
    nc = a+b-c*2
    nc %= mod
    nd = a*(h-1)+b*(w-1)+d*(h-2)+d*(w-2)-c*(w-1)-c*(h-1)
    nd %= mod
    dp[i+1] = [na, nb, nc, nd]

print(dp[-1][2] % mod)
# for i in range(k+1):
#     print(dp[i])
