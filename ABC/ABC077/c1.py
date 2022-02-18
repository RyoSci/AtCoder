n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ai = -1
ab = [0] * (n + 1)
for bi in range(n):
    while ai + 1 < n and a[ai + 1] < b[bi]:
        ai += 1
    ab[bi + 1] = ab[bi] + ai + 1

bi = -1
ans = 0
for ci in range(n):
    while bi + 1 < n and b[bi + 1] < c[ci]:
        bi += 1
    ans += ab[bi + 1]

print(ans)
