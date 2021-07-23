n = 10**5+1
prime = [1]*n
prime[0] = 0
prime[1] = 0

for i in range(2, n):
    if prime[i] == 0:
        continue
    j = 2
    while i*j < n:
        prime[i*j] = 0
        j += 1

memo = [0]*n
for i in range(n):
    if prime[i] == 1:
        if i % 2 == 1 and prime[(i+1) // 2] == 1:
            memo[i] = 1

dp = [0]*(n+1)
for i in range(n):
    dp[i+1] = dp[i]+memo[i]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(dp[r+1]-dp[l])
