n = int(input())
c = sorted(list(map(int, input().split())))

mod = 10**9+7
res = 1
for i in range(n):
    res *= c[i]-i
    res %= mod

print(res)
