n = int(input())
res = 1
mod = 10**9+7

for i in range(n):
    a = sum(list(map(int, input().split())))
    res = (res*a) % mod

print(res)
