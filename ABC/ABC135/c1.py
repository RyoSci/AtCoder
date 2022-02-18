n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

defeat_monster = 0
for i in range(n):
    defeat_monster += min(b[i], a[i])
    defeat_monster += min(b[i] - min(b[i], a[i]), a[i + 1])
    a[i + 1] -= min(b[i] - min(b[i], a[i]), a[i + 1])

print(defeat_monster)