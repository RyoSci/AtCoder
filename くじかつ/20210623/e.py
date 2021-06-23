from bisect import bisect_left
a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]

for xi in x:
    res = 10**11
    sr = bisect_left(s, xi)
    tr = bisect_left(t, xi)
    sl = max(0, sr-1)
    tl = max(0, tr-1)
    sr = min(sr, a-1)
    tr = min(tr, b-1)
    for si in [sl, sr]:
        for ti in [tl, tr]:
            if s[si] <= xi <= t[ti]:
                tmp = t[ti]-s[si]+min(t[ti]-xi, xi-s[si])
            elif t[ti] <= xi <= s[si]:
                tmp = s[si]-t[ti]+min(s[si]-xi, xi-t[ti])
            else:
                tmp = max(abs(xi-s[si]), abs(xi-t[ti]))
            res = min(res, tmp)
    print(res)
