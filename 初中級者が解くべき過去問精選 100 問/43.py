import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
s = [list(input().strip()) for _ in range(5)]

rbw = [[0]*3 for _ in range(n+1)]

for i in range(5):
    for j in range(n):
        # rbwを１インデックスに合わせる
        if s[i][j] == "R":
            rbw[j+1][0] += 1
        elif s[i][j] == "B":
            rbw[j+1][1] += 1
        elif s[i][j] == "W":
            rbw[j+1][2] += 1


INF = 10**18
dp = [[INF]*3 for _ in range(n+1)]
# 初期化　
# 最初の列は白紙でよく、0とする。
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

# i番目の列がj色で塗られるときのそれまでの更新回数の最小値
for i in range(1, n+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1) % 3]+5-rbw[i][j],
                       dp[i-1][(j+2) % 3]+5-rbw[i][j])


print(min(dp[n]))
