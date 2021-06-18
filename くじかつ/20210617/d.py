n = int(input())
ans = set()


def dfs(s):
    if len(s) == n:
        print(s)
        return
    for i in range(len(set(s))+1):
        dfs(s+chr(ord("a")+i))


dfs("a")
