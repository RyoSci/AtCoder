n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

a_b = 2*10**5
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a_b = min(a_b, max(a[i], b[j]))
    a_b = min(a_b, a[i]+b[i])

print(a_b)
