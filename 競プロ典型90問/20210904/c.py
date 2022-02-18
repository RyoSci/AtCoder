import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, w = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(h)]

res = 0
for i in range(1 << h):
    a = [0]*h
    for j in range(h):
        if i >> j & 1:
            a[j] = 1
    cnt = dict()
    for j in range(w):
        col = dict()
        for k in range(h):
            if a[k]:
                if p[k][j] not in col:
                    col[p[k][j]] = 0
                col[p[k][j]] += 1
        if len(col) == 1:
            key = list(col.keys())[0]
            if key not in cnt:
                cnt[key] = 0
            cnt[key] += col[key]
    max_val = 0
    for val in cnt.values():
        max_val = max(max_val, val)

    res = max(res, max_val)


print(res)
