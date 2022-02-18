n, x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
counter = 1
for i in range(n):
    d += l[i]
    if d <= x:
        counter += 1

print(counter)