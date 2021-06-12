n, q = map(int, input().split())
a = list(map(int, input().split()))
dis = [a[i] - a[i+1] for i in range(n-1)]
total = sum(abs(dis[i]) for i in range(n-1))

for j in range(q):
    l, r, v = map(int, input().split())
    if l >= 2:
        total -= abs(dis[l-2])
        dis[l-2] -= v
        total += abs(dis[l-2])
    if r <= n-1:
        total -= abs(dis[r-1])
        dis[r-1] += v
        total += abs(dis[r-1])
    print(total)
