n = int(input())
a = []
b = []
a_b = 2*10**5
for i in range(n):
    ai, bi = map(int, input().split())
    a.append([ai, i])
    b.append([bi, i])
    a_b = min(a_b, ai+bi)

a.sort()
b.sort()

if a[0][1] == b[0][1]:
    a_b = min(a_b, max(a[0][0], b[1][0]), max(a[1][0], b[0][0]))
else:
    a_b = min(a_b, max(a[0][0], b[0][0]))

print(a_b)
