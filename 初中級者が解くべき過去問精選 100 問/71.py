n, q = map(int, input().split())
a = list(map(int, input().split()))
c = [1]+list(map(int, input().split()))+[1]

mod = 10**9+7

dis = [0]*n
for i in range(n-1):
    dis[i+1] = dis[i]+pow(a[i], a[i+1], mod)
    dis[i+1] %= mod

res = 0
for i in range(q+1):
    # res += abs(dis[c[i+1]-1]-dis[c[i]-1])
    res += (dis[max(c[i+1], c[i])-1] - dis[min(c[i+1], c[i])-1]) % mod
    res %= mod

print(res)
