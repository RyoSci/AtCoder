from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

res = 0
for a in combinations_with_replacement(range(1, m+1), n):
    tmp = 0
    for ai, bi, ci, di in abcd:
        if a[bi-1]-a[ai-1] == ci:
            tmp += di
    res = max(res, tmp)

print(res)
