l, r = map(int, input().split())
mod = 10**9+7
res = 0
for i in range(1, 20):
    if 10**i-1 < l or r < 10**(i-1):
        continue
    else:
        ll = max(l, 10**(i-1))
        rr = min(r, 10**i-1)
    tmp = i*(rr+ll)*((rr-ll)+1)//2
    res = (res+tmp) % mod
print(res)
