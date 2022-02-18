n, m  = map(int, input().split())
a_b = []

for i in range(n):
    a_b.append(list(map(int, input().split())))

a_b.sort()

res = 0
counter = 0
for i in range(n):
    counter = min(m, a_b[i][1])
    m -= counter
    res += counter * a_b[i][0]
    if m == 0:
        break
print(res)