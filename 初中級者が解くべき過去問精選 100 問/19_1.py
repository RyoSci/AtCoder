d = int(input())
n = int(input())
m = int(input())
shops = [0, d]
for i in range(n-1):
    shops.append(int(input()))
shops.sort()

order = [int(input()) for _ in range(m)]


def binary_search(x, i):
    l = 0
    r = len(x)-1
    m = (l+r)//2
    while l + 1 < r:
        if x[m] <= i:
            l = m
        else:
            r = m
        m = (l+r)//2
    return m


time = 0
for j in range(m):
    pos = binary_search(shops, order[j])
    time += min(abs(shops[pos]-order[j]), abs(shops[pos+1]-order[j]))

print(time)
