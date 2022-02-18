n, k = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]


def dfs(ans, i):
    if i == n:
        return ans == 0
    for j in range(k):
        dfs(ans ^ t[i][j], i + 1)


for ii in range(k):
    res = dfs(t[0][ii], 1)
    if res:
        print("Found")
        break
else:
    print("Nothing")
