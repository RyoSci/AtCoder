from bisect import bisect_left
d = int(input())
n = int(input())
m = int(input())
shops = [0, d]
for i in range(n-1):
    shops.append(int(input()))
shops.sort()

order = [int(input()) for _ in range(m)]

time = 0
for j in range(m):
    pos = bisect_left(shops, order[j])
    time += min(abs(shops[pos-1]-order[j]), abs(shops[pos]-order[j]))

print(time)
