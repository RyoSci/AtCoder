n, m, k = map(int, input().split())
sum_set = set()

for i in range(m + 1):
    for j in range(n + 1):
        num = n * i + (m - 2 * i) * j
        sum_set.add(num)

if k in sum_set:
    print("Yes")
else:
    print("No")
