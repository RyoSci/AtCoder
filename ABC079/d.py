from itertools import permutations

h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
roots = []
for i in range(10):
    root = list(range(i)) + list(range(i + 1, 10))
    roots.append(root)


ans = [10 ** 4] * 10
for i in range(0, 10):
    if i == 1:
        continue
    root = roots[i]
    for j in permutations(root):
        tmp = c[i][j[0]]
        # j = [i] + list(j)
        for k in range(8):
            if j[k] == 1:
                ans[i] = min(ans[i], tmp)
                break
            if ans[j[k]] != 10 ** 4:
                tmp += ans[j[k]]
                ans[i] = min(ans[i], tmp)
                break
            tmp += c[j[k]][j[k + 1]]

a = [list(map(int, input().split())) for i in range(h)]
res = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1 and a[i][j] != 1:
            res += ans[a[i][j]]

print(res)
