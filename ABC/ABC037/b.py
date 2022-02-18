n, q = map(int, input().split())
a = [0] * n
for i in range(q):
    l, r, q = map(int, input().split())
    for j in range(l, r + 1):
        a[j - 1] = q

for i in range(n):
    print(a[i])
