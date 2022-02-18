import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353

for i in range(1, n):
    a[0] -= a[i]


if a[0] < k:
    print(0)
    exit()
a[0] -= k

ans = 1
for i in range(n):
    ans = ans*pow(k, a[i], mod) % mod

print(ans % mod)
