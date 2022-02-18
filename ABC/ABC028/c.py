abcde = list(map(int, input().split()))
res = []
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i == j or j == k or k == i:
                continue
            else:
                if abcde[i] + abcde[j] + abcde[k] not in res:
                    res.append(abcde[i] + abcde[j] + abcde[k])

res.sort(reverse=True)
print(res[2])
