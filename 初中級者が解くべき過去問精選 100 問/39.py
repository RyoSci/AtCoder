n = int(input())
a = list(map(int, input().split()))

dp = [[0]*21 for _ in range(n)]
dp[1][a[0]] = 1

for i in range(n-1):
    for j in range(21):
        if dp[i][j] == 0:
            continue
        for k in [-1, 1]:
            if 0 <= j+a[i]*k <= 20:
                dp[i+1][j+a[i]*k] += 1*dp[i][j]

print((dp[-1][a[-1]]))
