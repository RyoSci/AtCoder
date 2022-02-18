from sys import setrecursionlimit
setrecursionlimit(10**7)

n = int(input())


def dfs(s, i, max_l):
    if i == n:
        print(s)
        return
    for j in range(max_l+1):
        max_l = max(max_l, j+1)
        dfs(s+chr(j+ord("a")), i+1, max_l)


dfs("", 0, 0)
