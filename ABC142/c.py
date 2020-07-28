n = int(input())
a = list(map(int, input().split()))

order = [0] * (n + 1)
for i in range(n):
    order[a[i]] = i + 1

print(*order[1:])
