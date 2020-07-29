l, r = map(int, input().split())
if r - l >= 2018:
    print(0)
else:
    min_ij = 2018
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            min_ij = min(min_ij, ((i % 2019) * (j % 2019)) % 2019)
    print(min_ij)