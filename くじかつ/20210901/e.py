import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

tmp = []
for i in range(x):
    for j in range(y):
        tmp.append(a[i]+b[j])

tmp.sort(reverse=True)
tmp = tmp[:min(x*y, k)]

res = []
for i in range(z):
    for j in tmp:
        res.append(c[i]+j)

res.sort(reverse=True)

print(*res[:k], sep="\n")
