n = int(input())


def dfs(s, i):
    if i == n:
        print(s)
        return 0
    for j in "abc":
        dfs(s + j, i + 1)


dfs("", 0)
