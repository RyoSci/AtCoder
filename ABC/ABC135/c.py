n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

monster = sum(a)
for i in range(n):
    a[i + 1] -= min(b[i] - min(b[i], a[i]), a[i + 1])
    a[i] -= min(b[i], a[i])

print(monster - sum(a))

