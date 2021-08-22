from bisect import bisect_right

n, k, p = map(int, input().split())
a = list(map(int, input().split()))
n_ = n//2
_n = n-n_
a_ = a[:n_]
_a = a[n_:]

d_ = [[] for _ in range(n_+1)]

for i in range(1 << n_):
    res = 0
    cnt = 0
    for j in range(n_):
        if i >> j & 1:
            res += a_[j]
            cnt += 1
    d_[cnt].append(res)

for i in range(n_):
    d_[i].sort()


ans = 0
for i in range(1 << _n):
    res = 0
    cnt = 0
    for j in range(_n):
        if i >> j & 1:
            res += _a[j]
            cnt += 1
    if 0 <= k-cnt <= n_:
        r = bisect_right(d_[k-cnt], p-res)
        ans += r

print(ans)
