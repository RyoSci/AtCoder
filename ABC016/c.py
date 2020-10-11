n, m = map(int, input().split())
sns = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    sns[a - 1][b - 1] = 1
    sns[b - 1][a - 1] = 1

for i in range(n):
    res = set()
    for j in range(n):
        if i == j:
            continue
        elif sns[i][j] == 1:
            for k in range(n):
                if k == j or i == k:
                    continue
                elif sns[j][k] == 1 and sns[i][k] == 0:
                    res.add(k)
    print(len(res))
