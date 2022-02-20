import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x = map(int, input().split())

ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a,b])

dp=[[0]*(x+1) for _ in range(n+1)]

# dp[i][j]<-i番目にjにいることができるかどうか
dp[0][0]=1
for i in range(n):
    for j in range(x+1):
        if dp[i][j]==0:
            continue
        for k in ab[i]:
            if j+k<=x:
                dp[i+1][j+k] = 1


if dp[n][x]:
    print("Yes")
else:
    print("No")