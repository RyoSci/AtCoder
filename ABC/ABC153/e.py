h, n = map(int, input().split())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

knapsack = [10 ** 9] * (h + 1)
knapsack[0] = 0

for i in range(h):
    for j in range(n):
        knapsack[min(h, i + a[j])] = min(knapsack[min(h, i + a[j])],
                                         knapsack[i] + b[j])

print(knapsack[h])
