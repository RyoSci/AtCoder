import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

cal = [0]*(n+1)

mod = 998244353
for i in range(1, n+1):
    cal[i] += cal[i-1]+s[i-1]
    cal[i] %= mod

for i in range(1, n+1):
    cal[i] += cal[i-1]
    cal[i] %= mod

d = dict()
i = 0
res = 0

for j in range(n):
    if a[j] not in d:
        d[a[j]] = j
    else:
        res += cal[len(d)]
        res -= cal[j-d[a[j]]-1]
        res %= mod
        while i < d[a[j]]:
            del d[a[i]]
            i += 1
        i += 1
        d[a[j]] = j

res += cal[len(d)]
print(res % mod)
