import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))


res = 0
d = dict()

l = 0
for r in range(n):
    if a[r] not in d:
        d[a[r]] = 0
    d[a[r]] += 1

    if len(d) > k:
        while l < n:
            d[a[l]] -= 1
            if d[a[l]] == 0:
                del d[a[l]]
                l += 1
                break
            l += 1
    else:
        res = max(res, r-l+1)

print(res)
