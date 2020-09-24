n = int(input())
a = list(map(int, input().split()))
a = [a[0]] + a
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = min(dp[i - 1] + abs(a[i] - a[i - 1]),
                dp[i - 2] + abs(a[i] - a[i - 2]))

print(dp[-1])
