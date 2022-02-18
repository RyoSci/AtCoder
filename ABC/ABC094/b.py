n, m, x = map(int, input().split())
a = list(map(int, input().split()))
counter = 0
for i in range(m):
    if a[i] > x:
        break
    counter += 1

res = min(counter, m-counter)
print(res)
