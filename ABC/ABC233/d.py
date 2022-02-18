import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
for i in range(n):
    a[i+1] += a[i]

d = dict()
for i in range(1, n+1):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

ans = 0
for i in range(n+1):
    if a[i]+k in d:
        if k == 0:
            ans += d[a[i]+k]-1
        else:
            ans += d[a[i]+k]
    if i == 0:
        continue
    d[a[i]] -= 1
    if d[a[i]] == 0:
        del d[a[i]]

print(ans)
