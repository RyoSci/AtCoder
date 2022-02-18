n = int(input())

# ni = 0
# while 1:
#     if 9**ni > n:
#         break
#     ni += 1

# si = 0
# while 1:
#     if 6**si > n:
#         break
#     si += 1


nine = [9**(i) for i in range(1, 6)]
six = [6**(i) for i in range(1, 7)]

total = [1]+nine+six

dp = [10**18]*(n+1)
dp[0] = 0
for i in range(n):
    for j in total:
        if i+j < n+1:
            dp[i+j] = min(dp[i]+1, dp[i+j])

print(dp[n])
