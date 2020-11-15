import itertools

n, k = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]

res = 0
for i in itertools.permutations(range(2, n + 1)):
    dis = 0
    now = 0
    for j in i:
        dis += t[now][j - 1]
        now = j - 1
    dis += t[now][0]
    if dis == k:
        res += 1

print(res)
