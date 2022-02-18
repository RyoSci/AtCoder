n, k = map(int, input().split())
l_r = [list(map(int, input().split())) for i in range(k)]
l_r.sort()
a = [0] * (n + 1)
a[1] = 1
s = [0] * (n + 1)
mod = 998244353

for i in range(1, n + 1):
    for j in range(k):
        if i - 1 < l_r[j][0]:
            break
        else:
            l = l_r[j][0]
            r = min(i, l_r[j][1])
            a[i] = (a[i] + s[i - l] - s[max(0, i - r - 1)]) % mod
    s[i] = (s[i - 1] + a[i]) % mod

print(a[-1])
