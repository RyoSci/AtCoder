n = int(input())
dish = []
for i in range(n):
    a, b = map(int, input().split())
    dish.append([a+b, a, b])

dish.sort(reverse=True)

res = 0
for i in range(n):
    if i % 2 == 0:
        res += dish[i][1]
    else:
        res -= dish[i][2]

print(res)
