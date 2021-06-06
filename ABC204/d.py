n = int(input())
t = list(map(int, input().split()))
t.sort()

dp = [[0 for _ in range(10**5+1)] for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(10**5+1):
        if dp[i][j] == 1 and j+t[i] <= 10**5:
            dp[i+1][j] = 1
            dp[i+1][j+t[i]] = 1

res_num = 0
near = 10**6
total = sum(t)
for i in range(10**5+1):
    if dp[n][i] == 1:
        if near > abs(total - 2 * i):
            near = abs(total - 2 * i)
            res_num = i

print(max(res_num, abs(total-res_num)))
