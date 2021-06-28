n = int(input())

memo = [-1]*100


def dfs(x):
    if memo[x] != -1:
        return memo[x]
    if x == 0 or x == 1:
        return 1
    memo[x] = dfs(x-1)+dfs(x-2)
    return memo[x]


print(dfs(n))
