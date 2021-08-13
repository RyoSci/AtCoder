n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

a = []


def dfs(s, n):
    if n == 0:
        a.append(s)
        return
    for i in range(s[-1], m+1):
        dfs(s+[i], n-1)


for i in range(1, m+1):
    dfs([i], n-1)

res = 0
for s in a:
    tmp = 0
    for ai, bi, ci, di in abcd:
        if s[bi-1]-s[ai-1] == ci:
            tmp += di
    res = max(res, tmp)

print(res)
