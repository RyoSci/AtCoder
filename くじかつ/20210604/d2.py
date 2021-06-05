a, b, k = map(int, input().split())


def combination(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res *= i
    for i in range(k, 0, -1):
        res //= i
    return res


dp = [[0 for j in range(61)] for i in range(61)]

for i in range(61):
    for j in range(61):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]


def dfs(a, b, s, n, i):
    if a == 0 or b == 0:
        return s + "a"*a + "b"*b
    left = dp[a+b-1][a-1]
    right = dp[a+b-1][b-1]

    if k <= left + i:
        res = dfs(a-1, b, s+"a", left, i)
    else:
        res = dfs(a, b-1, s+"b", right, i+left)
    return res


n = combination(a+b, a)

res = dfs(a, b, "", n, 0)
print(res)
