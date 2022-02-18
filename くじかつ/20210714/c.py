n = int(input())
a = list(map(int, input().split()))

p = [0]*n
m = [0]*n
p[0] = 1
m[0] = 1

mod = 10**9+7
for i in range(1, n):
    p[i] = p[i-1]+m[i-1]
    p[i] %= mod
    m[i] = p[i-1]
    m[i] %= mod


res = a[0]*p[-1]
res %= mod
for i in range(1, n):
    res = res+p[i-1]*p[-i-1]*a[i]-m[i-1]*m[-i-1]*a[i]
    res %= mod
print(res)
