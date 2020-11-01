n = int(input())
dp = [100001] * 100001
dp[0] = 0
# dp[1] = 1

# for nine in range(1, 7):
#     for i in range(1, 9):
#         if 9 ** nine * i <= 100000:
#             dp[9 ** nine * i] = min(dp[9 ** nine * i], i)

# for six in range(1, 8):
#     for i in range(1, 6):
#         if 6 ** six * i <= 100000:
#             dp[6 ** six * i] = min(dp[6 ** six * i], i)

for i in range(1, n + 1):
    for nine in range(1, 7):
        if 9 ** nine <= i:
            dp[i] = min(dp[i - 9 ** nine] + 1, dp[i])
        else:
            break
    for six in range(1, 8):
        if 6 ** six <= i:
            dp[i] = min(dp[i - 6 ** six] + 1, dp[i])
        else:
            break
    dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[n])
