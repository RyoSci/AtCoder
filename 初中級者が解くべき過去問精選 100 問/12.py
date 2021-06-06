n, m = map(int, input().split())

relations = [set() for _ in range(n)]
for i in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    relations[x].add(y)
    relations[y].add(x)

res = 1
for i in range(1 << n):
    candidate = []
    for j in range(n):
        if i >> j & 1:
            candidate.append(j)
    k = len(candidate)
    flag = False
    for j in range(k-1):
        for jj in range(j+1, k):
            if not candidate[j] in relations[candidate[jj]]:
                flag = True
                break
        if flag:
            break
    else:
        res = max(res, len(candidate))

print(res)
