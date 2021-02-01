n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a + b, [a, b]])

ab.sort(reverse=True)

res = 0
for i in range(n):
    if i % 2 == 0:
        res += ab[i][1][0]
    else:
        res -= ab[i][1][1]

print(res)
