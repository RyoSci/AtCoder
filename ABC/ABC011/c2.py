n = int(input())
dp = [101] * (301)
for i in range(3):
    ng = int(input())
    dp[ng] = "NG"
start = True
if dp[n] == "NG":
    start = False
else:
    dp[n] = 0

for i in range(n, 2, -1):
    if dp[i] == "NG":
        pass
    else:
        is_not_rewrite = True
        for j in range(3, 0, -1):
            if dp[i - j] == "NG":
                pass
            else:
                dp[i - j] = min(dp[i - j], dp[i] + 1)
                is_not_rewrite = False
        if is_not_rewrite or not start:
            print("NO")
            break
else:
    if dp[1] == "NG":
        dp[1] = 101
    if dp[2] == "NG":
        dp[2] = 101
    dp[0] = min(dp[0], dp[1] + 1, dp[2] + 1)
    if dp[0] <= 100:
        print("YES")
    else:
        print("NO")
