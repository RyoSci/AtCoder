import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
mod = 10**9+7

res = 0
for i in range(k, n+2):
    res += i*(n+n-i+1)//2-i*(i-1)//2+1
    res %= mod
print(res)
